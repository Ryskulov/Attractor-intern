import handler_methods
from method import HTTP_METHODS
from router import Url

patterns = [
    Url(HTTP_METHODS.GET, '/static/', handler_methods.static),
    Url(HTTP_METHODS.GET, '/media/', handler_methods.media),
    Url(HTTP_METHODS.GET, '/post/edit/\d+/', handler_methods.post_edit_render),
    Url(HTTP_METHODS.POST, '/update/', handler_methods.post_edit),
    Url(HTTP_METHODS.GET, '/post/\d+/', handler_methods.post_detail),
    Url(HTTP_METHODS.GET, '/delete/post/\d+/', handler_methods.post_delete),
    Url(HTTP_METHODS.GET, '/signup/', handler_methods.signup_render),
    Url(HTTP_METHODS.POST, '/signup/', handler_methods.signup),
    Url(HTTP_METHODS.GET, '/create/', handler_methods.create_post_render),
    Url(HTTP_METHODS.POST, '/create/', handler_methods.create_post),
    Url(HTTP_METHODS.GET, '/login/', handler_methods.login_render),
    Url(HTTP_METHODS.POST, '/login/', handler_methods.login),
    Url(HTTP_METHODS.GET, '/logout/', handler_methods.logout),
    Url(HTTP_METHODS.GET, '/', handler_methods.index),
]
