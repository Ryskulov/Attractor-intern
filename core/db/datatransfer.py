# from method import method_post
# import uuid


class DataTransfer():

    def get_signup_param(self, request):
        user_attribute = method_post(request)
        return self

    def get_signup_param(self):
        user_attribute = {'username': 'admin', 'password': 'password'}
        a = user_attribute['username']
        return user_attribute


test = DataTransfer()

def dat():
    print(test.get_signup_param())
    a = test.get_signup_param()
    b = a['username']
    c = a['password']
    print(b, c)
    return b, c



dat()




# class qwe():
#     username = 'erwt'
#     login = 'fsfas'
#
# def asd(obj):
#     print(obj.username)
#     print(obj.login)
#
#
# def zxc():
#     asd(qwe)
#
# zxc()



users = {'user': {
            '1': ['fasdfadsf', 'sdfas fasf asfasdf asfas fasdf'],
            '2': ['title', 'description'],
            '3': ['title', 'description'],},
        'user': {
                    '1': ['fasdfadsf', 'sdfas fasf asfasdf asfas fasdf'],
                    '2': ['title', 'description'],
                    '3': ['title', 'description'],},
},
