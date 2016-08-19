import uuid
import settings
import mimetypes
from http import HTTPStatus
from cookies import Cookie
from method import method_post
from db.database import DataAccessLayer
from template_code.template import Templates


def handle_404(request):
    html = Templates('404.html').render()
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def static(request):
    file_path = request.path
    try:
        file = open(settings.STATIC_DIR + request.path, "rb")
    except IOError:
        request.send_error(404, 'File Not Found: %s ' % file_path)
    else:
        request.send_response(200)
        mime_type, _ = mimetypes.guess_type(file_path)
        request.send_header('Content-type', mime_type)
        request.end_headers()
        for items in file:
            request.wfile.write(items)


def media(request):
    file_path = request.path
    try:
        file = open(settings.MEDIA_DIR + request.path, "rb")
    except IOError:
        request.send_error(404, 'File Not Found: %s ' % file_path)
    else:
        request.send_response(200)
        mime_type, _ = mimetypes.guess_type(file_path)
        request.send_header('Content-type', mime_type)
        request.end_headers()
        for items in file:
            request.wfile.write(items)


def index(request):
    dal = DataAccessLayer()
    cookie = Cookie
    request.send_response(HTTPStatus.OK)
    if cookie.cookie_dict.get('session'):
        status = True
        create = True
    else:
        status = False
        create = False
    post_html = dal.get_all_posts()
    html = Templates('index.html').render(
        status=status, create_post=create, blog=post_html
    )
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def signup_render(request):
    html = Templates('register.html').render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def signup(request):
    dal = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if dal.create_user(request):
        print("Create success new login")
        request.send_header('Location', '/login/')
    else:
        request.send_header('Location', '/signup/')
        print("Login don't register")
    request.send_header('Content-Type', 'text/html')
    html = Templates('login.html').render()
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def login_render(request):
    cookie = Cookie
    html = Templates('login.html').render()
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
    dal = DataAccessLayer()
    user_attribute = method_post(request)
    username = user_attribute['username']
    password = user_attribute['password']
    request.send_response(HTTPStatus.SEE_OTHER)
    sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, username).hex)
    if dal.check_user_is_exist(username, password):
        cookie = Cookie()
        cookie.create_cookie('session', sid)
        request.send_header('Location', '/')
        request.send_header('Set-Cookie', '%s=%s; path=/;' % ('session', sid))
        print("Login Success")
    else:
        request.send_header('Content-Type', 'text/html')
        print("Login Error")
    request.end_headers()
    html = Templates('login.html').render()
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
    if cookie.cookie_dict.get('session'):
        login = True
        request.send_response(HTTPStatus.OK)
        request.send_header('Content-Type', 'text/html')
    else:
        login = False
        request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
        request.send_header('Location', '/login/')
    html = Templates('create_post.html').render(
        login=login
    )
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def create_post(request):
    dal = DataAccessLayer()
    cookie = Cookie
    if cookie.cookie_dict['session']:
        login = True
    else:
        login = False
    dal.create_post(request)
    html = Templates('create_post.html').render(login=login)
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', '/')
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
    html = Templates('post_detail.html').render(
        login=login, post_edit=post_edit, blog=post
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
        html = Templates('post_edit.html').render(post=post)
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
    dal = DataAccessLayer()
    blog_attribute = method_post(request)
    id = blog_attribute['id']
    title = blog_attribute['title']
    description = blog_attribute['description']
    picture = '/media/uploads/photo%s.jpeg' % id
    f = open('.' + picture, 'w+b')
    f.write(blog_attribute['picture'])
    f.close()
    picture = picture[6:]
    dal.update_post_by_id(id=id, title=title,
                         description=description, picture=picture)
    post = dal.get_post_by_id(id)
    html = Templates('post_edit.html').render(post=post)
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', '/post/%s/' % id)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def post_delete(request):
    id = get_id_from_url(request)
    dal = DataAccessLayer()
    dal.delete_post_by_id(id)
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', '/')
    request.end_headers()
    return request


def get_id_from_url(request):
    url_index = -2
    return int(request.path.split('/')[url_index])