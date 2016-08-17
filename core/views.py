from http import HTTPStatus

import settings
import mimetypes
import uuid
from db.database import User, Cookie, Post, DataAccessLayer
from template_code.template import Template, post, Templates, gete_parse_url


def handle_404(request):
    context = {'not-found': 'File Not found'}
    html = Template('404.html', context).render()
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def static(request):
    try:
        filepath = request.path
        f = open(settings.STATIC_DIR+request.path, "rb")
    except IOError:
        request.send_error(404, 'File Not Found: %s ' % filepath)
    else:
        request.send_response(200)
        mimetype, _ = mimetypes.guess_type(filepath)
        request.send_header('Content-type', mimetype)
        request.end_headers()
        for s in f:
            request.wfile.write(s)


def media(request):
    try:
        filepath = request.path
        f = open(settings.MEDIA_DIR +request.path, "rb")
    except IOError:
        request.send_error(404, 'File Not Found: %s ' % filepath)
    else:
        request.send_response(200)
        mimetype, _ = mimetypes.guess_type(filepath)
        request.send_header('Content-type', mimetype)
        request.end_headers()
        for s in f:
            request.wfile.write(s)


def index(request):
    db = DataAccessLayer()
    cookie = Cookie
    request.send_response(HTTPStatus.OK)
    if cookie.cookie_dict.get('session'):
        status = True
        create_post = True
    else:
        status = False
        create_post = False
    f = open(settings.TEMPLATES_DIR + '/index.html')
    read = f.read()
    post_html = db.get_all_posts()
    html = Templates(read).render(status=status,
                                  create_post=create_post,
                                  blog=post_html
                                  )
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def signup_render(request):
    context = {}
    html = Template('register.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def signup(request):
    context = {}
    user_attribute = post(request)
    username = user_attribute.get('username')
    password = user_attribute.get('password')
    first_name = user_attribute.get('first_name')
    email = user_attribute.get('email')
    sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, username).hex)
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if not db.check_user_is_exist(username, password):
        db.create_user(username, password, first_name, email, sid)
        request.send_header('Location', '/login/')
        print("Create success new login")
    else:
        # request.send_header('Location', '/Error_signup/')
        request.send_header('Location', '/signup/')
        print("Login don't register")
    request.send_header('Content-Type', 'text/html')
    html = Template('login.html', context).render()
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def login_render(request):
    context = {}
    cookie = Cookie
    html = Template('login.html', context).render()
    if cookie.cookie_dict.get('session'):
        request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
        request.send_header('Location', '/')
    else:
        request.send_response(HTTPStatus.OK)
        request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def login(request):
    db = DataAccessLayer()
    context = {"error": ""}
    user_attribute = post(request)
    username = user_attribute.get('username')
    password = user_attribute.get('password')

    request.send_response(HTTPStatus.SEE_OTHER)
    print(username, 'eaedasdadad')
    sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, username).hex)
    if db.check_user_is_exist(username, password):
        cookie = Cookie()
        cookie.create_cookie('session', sid)
        request.send_header('Location', '/')
        request.send_header('Set-Cookie', '%s=%s; path=/;' % ('session', sid))
        print("Login Success")
    else:
        request.send_header('Content-Type', 'text/html')
        print("Login Error")
    request.end_headers()
    html = Template('login.html', context).render()
    request.wfile.write(str.encode(html))
    return request


def logout(request):
    cookie = Cookie
    cookie.cookie_dict.clear()
    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    if not cookie.cookie_dict:
        request.send_header('Set-Cookie', '%s=0; path=/;'
                            'Expires=Thu, 01 Jan 1970 00:00:00 GMT' % 'session')
        request.send_header('Location', '/login/')
        print('Logout succes')
    else:
        request.send_header('Content-Type', 'text/html')
    request.end_headers()


def create_post_render(request):
    cookie = Cookie
    f = open(settings.TEMPLATES_DIR + '/create_post.html')
    read = f.read()
    if cookie.cookie_dict.get('session'):
        login = True
        request.send_response(HTTPStatus.OK)
        request.send_header('Content-Type', 'text/html')
    else:
        login = False
        request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
        request.send_header('Location', '/login/')
    html = Templates(read).render(login=login)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def create_post(request):
    db = DataAccessLayer()
    id = db.create_id()
    cookie = Cookie
    if cookie.cookie_dict.get('session'):
        login = True
    else:
        login = False
    f = open(settings.TEMPLATES_DIR + '/create_post.html')
    read = f.read()
    request.send_response(HTTPStatus.SEE_OTHER)
    blog_attribute = post(request)
    title = blog_attribute.get('title')
    description = blog_attribute.get('description')
    picture = '/media/uploads/photo%s.jpeg' % id
    f = open('.' + picture, 'w+b')
    f.write(blog_attribute.get('picture'))
    f.close()
    picture = picture[6:]
    sid = cookie.cookie_dict.get('session')
    # begin_blog_length = len(db.get_title_post())
    db.create_post(id, title, description, picture, sid) #cookie.get_cookie.get('user_auth')
    # end_blog_length = len(db.get_title_post())
    # if end_blog_length > begin_blog_length:
    request.send_header('Location', '/')
    html = Templates(read).render(login=login)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_detail(request):
    db = DataAccessLayer()
    id = request.path.split('/')[-2]
    cookie = Cookie
    post = db.get_post_by_id(id)
    sid = post['sid']
    if cookie.cookie_dict.get('session'):
        login = True
    else:
        login = False
    if cookie.cookie_dict.get('session') == sid:
        post_edit = True
    else:
        post_edit = False
    f = open(settings.TEMPLATES_DIR + '/post_detail.html')
    read = f.read()
    html = Templates(read).render(login=login, post_edit=post_edit,
                                  blog=post
                                  )
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_edit_render(request):
    db = DataAccessLayer()
    cookie = Cookie
    id = request.path.split('/')[-2]
    post = db.get_post_by_id(id)

    sid = post['sid']
    if cookie.cookie_dict.get('session') == sid:
        f = open(settings.TEMPLATES_DIR + '/post_edit.html')
        read = f.read()
        html = Templates(read).render(post=post)
        request.send_response(HTTPStatus.OK)
        request.send_header('Content-Type', 'text/html')
        request.end_headers()
        request.wfile.write(str.encode(html))
    else:
        request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
        request.send_header('Location', '/')
        request.end_headers()
    return request


def post_edit(request):
    context = {}
    db = DataAccessLayer()
    html = Template('post_edit.html', context).render()
    request.send_response(HTTPStatus.SEE_OTHER)
    blog_attribute = post(request)
    id = blog_attribute.get('id')
    title = blog_attribute.get('title')
    description = blog_attribute.get('description')
    picture = '/media/uploads/photo%s.jpeg' % id
    f = open('.' + picture, 'w+b')
    f.write(blog_attribute.get('picture'))
    f.close()
    picture = picture[6:]
    db.update_post_by_id(id, title, description, picture)
    request.send_header('Location', '/post/%s/' % id)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_delete(request):
    id = request.path.split('/')[-2]
    db = DataAccessLayer()
    db.delete_post_by_id(id)
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', '/')
    request.end_headers()
    return request