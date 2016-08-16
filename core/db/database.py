# coding: utf-8


class User:
    username = ['admin']
    password = ['admin']
    first_name = []
    email = []

    def create_login(self, username, password, first_name, email):
        self.username.append(username)
        self.password.append(password)
        self.first_name.append(first_name)
        self.email.append(email)
        print (self.username)

    def check_user_is_exist(self, username, password):
        if username in self.username:
            index_username = self.username.index(username)
            if self.password[index_username] == password:
                return True
        return False

    def __get__(self):
        return self.username


class Blog:
    id = [1, 2, 3]
    title = ['Fully Baked up', 'Fully Baked up', 'Fully Baked up']
    description = ['Curabitur tincidunt dapibus odio, eu gravida felis blandit vel.'
                   'Vivamus feugiat auctor lorem non eleifend. Nam eu pellentesque'
                   'est, vitae interdum nisi.',
                   'Curabitur tincidunt dapibus odio, eu gravida felis blandit vel.'
                   'Vivamus feugiat auctor lorem non eleifend. Nam eu pellentesque est,'
                   'vitae interdum nisi.',
                   'Curabitur tincidunt dapibus odio, eu gravida felis blandit vel.'
                   'Vivamus feugiat auctor lorem non eleifend. Nam eu pellentesque est,'
                   'vitae interdum nisi.'
                   ]
    picture = ['/static/uploads/photo1.jpeg', '/static/uploads/photo1.jpeg',
               '/static/uploads/photo1.jpeg']
    sid = ['bace070115e3514497c547487d543032',
           'bace070115e3514497c547487d543032',
           'bace070115e3514497c547487d543032']

    def create_blog(self, id, title, description, picture, sid):
        self.id.append(id)
        self.title.append(title)
        self.description.append(description)
        self.picture.append(picture)
        self.sid.append(sid)
        print('CREATE POST %s' % self.sid)

    def get_blog_by_id(self, id):
        if not id in self.id:
            return 'Error %s' % id
        else:
            blog_index_id = self.id.index(id)
            title = self.title[blog_index_id]
            description = self.description[blog_index_id]
            picture = self.picture[blog_index_id]
            return title, description, picture


class Cookie:
    cookie_dict = {}

    def create_cookie(self, cookie_key, cookie_value):
        self.cookie_dict[cookie_key] = cookie_value

    def get_cookie(self, cookie_key, cookie_value):
        self.cookie_dict[cookie_key] = cookie_value

    def __get__(self):
        return self.cookie_dict


class DataAccessLayer:
    def __init__(self):
        self.user = User()
        self.blog = Blog()

    def create_user(self, username, password, first_name, email):
        self.user.create_login(username, password, first_name, email)

    def check_user_is_exist(self, username, password):
        return self.user.check_user_is_exist(username, password)

    def create_post(self, id, title, description, picture, sid):
        self.blog.create_blog(id, title, description, picture, sid)

    def get_post_by_id(self, id):
        return self.blog.get_blog_by_id(id)

    def get_title_post(self):
        return self.blog.title

    def get_username(self):
        return self.user.username

    def create_id(self):
        b = self.blog.id.pop()
        self.blog.id.append(b)
        id = b + 1
        return id

    def get_all_post(self):
        if len(self.blog.id) >= 1:
            return self.blog
        else:
            self.blog.id.append(1)
            self.blog.title.append('НЕ дам себя удалить! ')
            self.blog.description.append('Пожалуйста! Не удаляйте меня! Я последний из своего рода!!!!!!!')
            self.blog.picture.append('/static/uploads/danger.jpg')
            self.blog.sid.append('fadfasdfa342123311312')

    def get_post_id(self, id):
        id = self.blog.id.index(id)
        return id

    def edit_post_by_id(self, id):
        if not id in self.blog.id:
            return "error %s " % id
        else:
            blog_index_id = self.blog.id.index(id)
            title = self.blog.title[blog_index_id]
            description = self.blog.description[blog_index_id]
            picture = self.blog.picture[blog_index_id]
            sid = self.blog.sid[blog_index_id]
            return title, description, picture, sid

    def update_post_by_id(self, id, title, description, picture):

        if not id in self.blog.id:
            blog_index_id = self.blog.id.index(int(id))
            self.blog.title[blog_index_id] = title
            self.blog.description[blog_index_id] = description
            self.blog.picture[blog_index_id] = picture

        else:
            return "error %s " % id

    def delete_post_by_id(self, id):
        blog_index_id = self.blog.id.index(int(id))
        del self.blog.id[blog_index_id]
        del self.blog.description[blog_index_id]
        del self.blog.title[blog_index_id]
        del self.blog.picture[blog_index_id]
