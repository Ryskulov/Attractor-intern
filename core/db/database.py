# coding: utf-8
from exceptions import PostDoesNotExist
from method import method_post
import uuid
from cookies import Cookie


class User:
    dict_users = [
        {
            'username': 'admin',
            'password': 'admin',
            'first_name': 'Chingiz',
            'email': 'chingizkg@gmail.com',
            'sid': 'bace070115e3514497c547487d543032',
        },
        {
            'username': 'excrat',
            'password': 'password',
            'first_name': 'Chingiz',
            'email': 'chingizkg@gmail.com',
            'sid': 'bace070115e3514497c547487d543032',
        },
    ]


class Post:
    dict_posts = [
        {
            'id': 1,
            'title': 'Fully Baked up',
            'description': 'Curabitur tincidunt dapibus odio, eu gravida felis'
                           'blandit vel.Vivamus feugiat auctor lorem non eleifend.'
                           'Nam eu pellentesque est, vitae interdum nisi.',
            'picture': '/uploads/photo1.jpg',
            'sid': 'bace070115e3514497c547487d543032',
        },
        {
            'id': 2,
            'title': 'Fully Title blog',
            'description': 'Curabitur tincidunt dapibus odio, eu gravida felis'
                           'blandit vel.Vivamus feugiat auctor lorem non eleifend.'
                           'Nam eu pellentesque est, vitae interdum nisi.',
            'picture': '/uploads/photo2.jpg',
            'sid': 'bace070115e3514497c547487d543032',
        },
        {
            'id': 3,
            'title': 'Test Baked blog',
            'description': 'Curabitur tincidunt dapibus odio, eu gravida felis'
                           'blandit vel.Vivamus feugiat auctor lorem non eleifend.'
                           'Nam eu pellentesque est, vitae interdum nisi.',
            'picture': '/uploads/photo3.jpg',
            'sid': 'bace070115e3514497c547487d543032',
        }
    ]


class DataAccessLayer:

    count_for_id = [3]

    def __init__(self):
        self.user = User()
        self.post = Post()

    def create_id(self):
        just_one = 1
        self.count_for_id[0] += just_one
        return sum(self.count_for_id)

    def create_user(self, request):
        login_length = 2
        user_attr = method_post(request)
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, user_attr['username']).hex)
        if len(user_attr['username']) >= login_length:
            for item in self.user.dict_users:
                if item['username'] != user_attr['username']:
                    self.user.dict_users.append({
                        'username': user_attr['username'],
                        'password': user_attr['password'],
                        'first_name': user_attr['first_name'],
                        'email': user_attr['email'],
                        'sid': sid,
                    })
            return True

    def check_user_is_exist(self, username, password):
        for item in self.user.dict_users:
            if item['username'] == username:
                if item['password'] == password:
                    return True

    def get_all_posts(self):
        return self.post.dict_posts

    def create_post(self, request):
        id = self.create_id()
        blog_attr = method_post(request)
        picture = '/media/uploads/photo%s.jpeg' % id
        f = open('.' + picture, 'w+b')
        f.write(blog_attr['picture'])
        f.close()
        picture = picture[6:]
        cookie = Cookie
        sid = cookie.cookie_dict['session']
        self.post.dict_posts.append({
            'id': id,
            'title': blog_attr['title'],
            'description': blog_attr['description'],
            'picture': picture,
            'sid': sid
        })
        return self.get_post_by_id(id)

    def get_post_by_id(self, id):
        for item in self.post.dict_posts:
            if item['id'] == int(id):
                return item
        raise PostDoesNotExist()

    def update_post_by_id(self, **kwargs):
        for item in self.post.dict_posts:
            if item['id'] == int(kwargs['id']):
                item['title'] = kwargs['title']
                item['description'] = kwargs['description']
                item['picture'] = kwargs['picture']
                return item
        raise PostDoesNotExist()

    def delete_post_by_id(self, id):
        for item in self.post.dict_posts:
            if item['id'] == int(id):
                self.post.dict_posts.remove(item)
        return 'Deleted'
