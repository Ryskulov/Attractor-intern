from http import HTTPStatus, cookies

import settings
import mimetypes
import uuid
from db.database import User, Cookie, Blog, DataAccessLayer
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


def index(request):
    db = DataAccessLayer()
    cookie = Cookie
    request.send_response(HTTPStatus.OK)
    # sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, username).hex)
    if cookie.get_cookie.get('session'):
        print(cookie.get_cookie.get('session'))
        status = True
        create_post = True
    else:
        status = False
        create_post = False
    f = open(settings.TEMPLATES_DIR + '/index.html')
    read = f.read()
    post_html = ''

    for i in range(len(db.getAllPost().id)):
        len_text = 100
        post_html += '<div class="post__box">'
        post_html += '  <a href="post/%s/" class="post__link">' % (db.getAllPost().id[i])
        post_html += '      <img src="%s" width="250" height="100" alt="" class="post_picture">' % (db.getAllPost().picture[i][7:])
        post_html += '      <strong>%s</strong></a>' %(db.getAllPost().title[i])
        if len(db.getAllPost().description[i]) > len_text:
            post_html += '  <p class="post__text">%s</p>' % (db.getAllPost().description[i][:100])
        else:
            post_html += '  <p class="post__text">%s</p>' % db.getAllPost().description[i]
        post_html += '</div>\n'

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
    db = DataAccessLayer()
    user_attribute = post(request)
    username = user_attribute.get('username')
    password = user_attribute.get('password')
    first_name = user_attribute.get('first_name')
    email = user_attribute.get('email')
    request.send_response(HTTPStatus.SEE_OTHER)
    if not db.CheckUserIsExist(username, password):
        db.CreateUser(username, password, first_name, email)
        request.send_header('Location', '/login/')
        print("Create success new login")
    else:
        # request.send_header('Location', '/Error_signup/')
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
    if cookie.get_cookie.get('session'):
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
    if db.CheckUserIsExist(username, password):
        cookie = Cookie()
        cookie.CreateCookie('session', sid)
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
    cookie.get_cookie.clear()
    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    if not cookie.get_cookie:
        request.send_header('Set-Cookie', '%s=0; path=/;'
                            'Expires=Thu, 01 Jan 1970 00:00:00 GMT' % 'session')
        request.send_header('Location', '/login/')
        print('Logout succes')
    else:
        request.send_header('Content-Type', 'text/html')
    request.end_headers()


def create_post(request):
    cookie = Cookie
    f = open(settings.TEMPLATES_DIR + '/create_post.html')
    read = f.read()
    if cookie.get_cookie.get('session'):
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


def create_blog_post(request):
    context = {}
    db = DataAccessLayer()
    cookie = Cookie
    if cookie.get_cookie.get('session'):
        login = True
    else:
        login = False
    id = db.createid()
    f = open(settings.TEMPLATES_DIR + '/create_post.html')
    read = f.read()
    request.send_response(HTTPStatus.SEE_OTHER)
    blog_attribute = post(request)
    title = blog_attribute.get('title')
    description = blog_attribute.get('description')
    picture = '/static/uploads/photo%s.jpeg' % id
    f = open('.' + picture, 'w+b')
    f.write(blog_attribute.get('picture'))
    f.close()
    sid = cookie.get_cookie.get('session')
    begin_blog_length = len(db.GetTitlePost())
    db.CreatePost(id, title, description, picture, sid) #cookie.get_cookie.get('user_auth')
    end_blog_length = len(db.GetTitlePost())
    if end_blog_length > begin_blog_length:
        request.send_header('Location', '/')
    html = Templates(read).render(login=login)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_detail(request):
    db = DataAccessLayer()
    id = request.path.split('/')[-2]
    cookie = Cookie
    title, description, picture, sid = db.EditPostById(int(id))
    if cookie.get_cookie.get('session'):
        login = True
    else:
        login = False
    if cookie.get_cookie.get('session') == sid:
        post_edit = True
    else:
        post_edit = False
    f = open(settings.TEMPLATES_DIR + '/post_detail.html')
    read = f.read()
    link_post_edit = '/post/edit/%s/' % id
    link_post_delete = '/delete/post/%s/' % id
    html = Templates(read).render(login=login, post_edit=post_edit,
                                  link_post_edit=link_post_edit, link_post_delete=link_post_delete,
                                  picture=picture[7:], title=title,
                                  description=description,
                                  )
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_edit(request):
    db = DataAccessLayer()
    cookie = Cookie
    id = request.path.split('/')[-2]
    title, description, picture, sid = db.EditPostById(int(id))
    edit_post_html = ''
    if cookie.get_cookie.get('session') == sid:
        edit_post_html += '<form method="POST" action="/update/" class="login__form" enctype="multipart/form-data">'
        edit_post_html += '<input type="hidden" value="%s" name="id" class="form__input"/><br/>' % id
        edit_post_html += '<input type="text" value="%s" name="title" class="form__input"/><br/>' % title
        edit_post_html += '<textarea cols="50" rows="10" id="description" name="description" class="form__input">%s</textarea> <br/>' % description
        edit_post_html += '<input type="file" name="picture" class="form__input"/> <br/>'
        edit_post_html += '<input type="submit" value="Update" class="form__btn" />'
        edit_post_html += '</form>'
    else:
        edit_post_html += '<h1>HAHAHAHA</h1>'
    f = open(settings.TEMPLATES_DIR + '/post_edit.html')
    read = f.read()
    html = Templates(read).render(post_edit=edit_post_html)
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_update(request):
    context = {}
    db = DataAccessLayer()
    html = Template('post_edit.html', context).render()
    request.send_response(HTTPStatus.SEE_OTHER)
    blog_attribute = post(request)
    id = blog_attribute.get('id')
    title = blog_attribute.get('title')
    description = blog_attribute.get('description')
    picture = '/static/uploads/photo%s.jpeg' % id
    f = open('.' + picture, 'w+b')
    f.write(blog_attribute.get('picture'))
    f.close()
    db.updatePostById(id, title, description, picture) #cookie.get_cookie.get('user_auth')
    request.send_header('Location', '/post/%s/' % id)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_delete(request):
    id = request.path.split('/')[-2]
    db = DataAccessLayer()
    db.deletePostById(int(id))
    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    request.send_header('Location', '/')
    request.end_headers()