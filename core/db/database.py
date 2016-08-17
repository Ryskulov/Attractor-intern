# coding: utf-8
from exceptions import PostDoesNotExist


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
            'picture': '/uploads/photo1.jpeg',
            'sid': 'bace070115e3514497c547487d543032',
        },
        {
            'id': 2,
            'title': 'Fully Title blog',
            'description': 'Curabitur tincidunt dapibus odio, eu gravida felis'
                           'blandit vel.Vivamus feugiat auctor lorem non eleifend.'
                           'Nam eu pellentesque est, vitae interdum nisi.',
            'picture': '/uploads/photo1.jpeg',
            'sid': 'bace070115e3514497c547487d543032',
        },
        {
            'id': 3,
            'title': 'Test Baked blog',
            'description': 'Curabitur tincidunt dapibus odio, eu gravida felis'
                           'blandit vel.Vivamus feugiat auctor lorem non eleifend.'
                           'Nam eu pellentesque est, vitae interdum nisi.',
            'picture': '/uploads/photo1.jpeg',
            'sid': 'bace070115e3514497c547487d543032',
        }
    ]


class Cookie:
    cookie_dict = {}

    def create_cookie(self, cookie_key, cookie_value):
        self.cookie_dict[cookie_key] = cookie_value

    def get_cookie(self, cookie_key, cookie_value):
        self.cookie_dict[cookie_key] = cookie_value

    def __get__(self):
        return self.cookie_dict


class DataAccessLayer:

    count_for_id = [3]

    def __init__(self):
        self.user = User()
        self.blog = Post()

    def create_id(self, id=0):
        id += 1
        self.count_for_id[0] += id
        return sum(self.count_for_id)

    def create_user(self, username, password, first_name, email, sid):
        self.user.dict_users.append({
            'username': username,
            'password': password,
            'first_name': first_name,
            'email': email,
            'sid': sid,
        })
        print(self.user.dict_users)

    def check_user_is_exist(self, username, password):
        for item in self.user.dict_users:
            if item['username'] == username:
                if item['password'] == password:
                    return True

    def get_username(self):
        return self.user.username

    def get_all_posts(self):
        return self.blog.dict_posts

    def create_post(self, id, title, description, picture, sid):
        self.blog.dict_posts.append({
            'id': id,
            'title': title,
            'description': description,
            'picture': picture,
            'sid': sid
        })
        return self.get_post_by_id(id)

    def get_post_by_id(self, id):
        for item in self.blog.dict_posts:
            if item['id'] == int(id):
                return item
        raise PostDoesNotExist()

    def update_post_by_id(self, id, title, description, picture):
        for item in self.blog.dict_posts:
            if item['id'] == int(id):
                item['title'] = title
                item['description'] = description
                item['picture'] = picture
                return item
        raise PostDoesNotExist()

    def delete_post_by_id(self, id):
        for item in self.blog.dict_posts:
            if item['id'] == int(id):
                self.blog.dict_posts.remove(item)
        return 'Deleted'
