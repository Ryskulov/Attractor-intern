# coding: utf-8

class User:
    username = ['admin']
    password = ['admin']
    first_name = []
    email = []

    def CreateLogin(self, username, password, first_name, email):
        self.username.append(username)
        self.password.append(password)
        self.first_name.append(first_name)
        self.email.append(email)
        print (self.username)

    def CheckUserIsExist(self, username, password):
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
    print( '%s ddadadadsa' % id)

    def CreateBlog(self, id, title, description, picture, sid):
        self.id.append(id)
        self.title.append(title)
        self.description.append(description)
        self.picture.append(picture)
        self.sid.append(sid)
        print('CREATE POST %s' % self.sid)


    def GetBlogById(self, id):
        if not id in self.id:
            return 'Error %s' % id
        else:
            blog_index_id = self.id.index(id)
            title = self.title[blog_index_id]
            description = self.description[blog_index_id]
            picture = self.picture[blog_index_id]
            return title, description, picture


class Cookie:
    get_cookie = {}

    def CreateCookie(self, cookie_key, cookie_value):
        self.get_cookie[cookie_key] = cookie_value
        print('wwwwww %s' % self.get_cookie)

    def GetCookie(self, cookie_key, cookie_value):
        self.get_cookie[cookie_key] = cookie_value

    def __get__(self, instance, owner):
        return self.get_cookie


class DataAccessLayer:
    def __init__(self):
        self.user = User()
        self.blog = Blog()

    def CreateUser(self, username, password, first_name, email):
        self.user.CreateLogin(username, password, first_name, email)

    def CheckUserIsExist(self, username, password):
        return self.user.CheckUserIsExist(username, password)

    def CreatePost(self, id, title, description, picture, sid):
        self.blog.CreateBlog(id, title, description, picture, sid)

    def GetPostById(self, id):
        return self.blog.GetBlogById(id)

    def GetTitlePost(self):
        return self.blog.title

    def getUserName(self):
        return self.user.username

    def createid(self):
        b = self.blog.id.pop()
        self.blog.id.append(b)
        id = b + 1
        return id

    def getAllPost(self):
        if len(self.blog.id) >= 1:
            return self.blog
        else:
            self.blog.id.append(1)
            self.blog.title.append('НЕ дам себя удалить! ')
            self.blog.description.append('Пожалуйста! Не удаляйте меня! Я последний из своего рода!!!!!!!')
            self.blog.picture.append('/static/uploads/danger.jpg')
            self.blog.sid.append('fadfasdfa342123311312')

    def getpostid(self, id):
        id = self.blog.id.index(id)
        print(id)
        return id

    def EditPostById(self, id):
        if not id in self.blog.id:
            return "error %s " % id
        else:
            blog_index_id = self.blog.id.index(id)
            title = self.blog.title[blog_index_id]
            description = self.blog.description[blog_index_id]
            picture = self.blog.picture[blog_index_id]
            sid = self.blog.sid[blog_index_id]
            return title, description, picture, sid

    def updatePostById(self, id, title, description, picture):

        if not id in self.blog.id:
            blog_index_id = self.blog.id.index(int(id))
            self.blog.title[blog_index_id] = title
            self.blog.description[blog_index_id] = description
            self.blog.picture[blog_index_id] = picture

        else:
            return "error %s " % id

    def deletePostById(self, id):
        blog_index_id = self.blog.id.index(int(id))
        del self.blog.id[blog_index_id]
        del self.blog.description[blog_index_id]
        del self.blog.title[blog_index_id]
        del self.blog.picture[blog_index_id]

    # def check_cookie(self):
