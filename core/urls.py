import views
from method import HTTP_METHODS
from router import Url

patterns = [
    Url(HTTP_METHODS.GET, '/static/', views.static),
    Url(HTTP_METHODS.GET, '/post/edit/\d+/', views.post_edit),
    Url(HTTP_METHODS.POST, '/update/', views.post_update),
    Url(HTTP_METHODS.GET, '/post/\d+/', views.post_detail),
    Url(HTTP_METHODS.GET, '/delete/post/\d+/', views.post_delete),
    Url(HTTP_METHODS.GET, '/signup/', views.signup_render),
    Url(HTTP_METHODS.POST, '/signup/', views.signup),
    Url(HTTP_METHODS.GET, '/create/', views.create_post),
    Url(HTTP_METHODS.POST, '/create/', views.create_blog_post),
    Url(HTTP_METHODS.GET, '/login/', views.login_render),
    Url(HTTP_METHODS.POST, '/login/', views.login),
    Url(HTTP_METHODS.GET, '/logout/', views.logout),
    Url(HTTP_METHODS.GET, '/', views.index),
]
