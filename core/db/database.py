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

    def create_user(self, **kwargs):
        login_length = 2
        if len(kwargs['username']) >= login_length:
            for item in self.user.dict_users:
                if item['username'] != kwargs['username']:
                    self.user.dict_users.append({
                        'username': kwargs['username'],
                        'password': kwargs['password'],
                        'first_name': kwargs['first_name'],
                        'email': kwargs['email'],
                        'sid': kwargs['sid'],
                    })
            return True

    def check_user_is_exist(self, username, password):
        for item in self.user.dict_users:
            if item['username'] == username:
                if item['password'] == password:
                    return True

    def get_all_posts(self):
        return self.post.dict_posts

    def create_post(self, **kwargs):

        self.post.dict_posts.append({
            'id': kwargs['id'],
            'title': kwargs['title'],
            'description': kwargs['description'],
            'picture': kwargs['picture'],
            'sid': kwargs['sid']
        })
        return self.get_post_by_id(kwargs['id'])

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
