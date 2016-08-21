import unittest
from db.database import DataAccessLayer


class TestUser(unittest.TestCase):

    def setUp(self):
        self.dal = DataAccessLayer()

    def tearDown(self):
        del self.dal

    def test_user_sign_in_true(self):
        self.assertTrue(self.dal.check_user_is_exist('admin', 'admin'))

    def test_user_sign_in_false(self):
        self.assertFalse(self.dal.check_user_is_exist('otherlogin', 'badpassword'))

    def test_user_signup_username_more_2_characters(self):
        self.dal.create_user(
            username='randomir', password='password',
            email='chingiz@gmail.com',
            sid='asd3421dasfsdfsfd',
            first_name='Chingiz',
        )
        self.assertEqual(self.dal.user.dict_users[2], {
            'username': 'randomir',
            'password': 'password',
            'email': 'chingiz@gmail.com',
            'sid': 'asd3421dasfsdfsfd',
            'first_name': 'Chingiz',
        })


    def test_user_signup_username_less_2_characters(self):
        self.assertFalse(self.dal.create_user(
            username='r',
            password='password',
            email='chingiz@gmail.com',
            sid='asd3421dasfsdfsfd',
            first_name='Chingiz',
        ))

    def test_user_signup_username_is_empty(self):
        self.assertFalse(self.dal.create_user(
            username='',
            password='password',
            email='chingiz@gmail.com',
            sid='asd3421dasfsdfsfd',
            first_name='Chingiz',
        ))

    def test_post_create_post(self):
        self.dal.create_post(
            id=4, title='title for test',
            description='some text in description for test',
            picture='/media/uploads/picture_name.jpeg',
            sid='sidnumber201231231',
        )
        self.assertEqual(self.dal.post.dict_posts[3], {
            'id': 4,
            'title': 'title for test',
            'description': 'some text in description for test',
            'picture': '/media/uploads/picture_name.jpeg',
            'sid': 'sidnumber201231231',
        })

    def test_get_post_by_id(self):
        self.dal.get_post_by_id(3)
        self.assertEqual(self.dal.post.dict_posts[1], {
            'id': 2,
            'title': 'Fully Title blog',
            'description': 'Curabitur tincidunt dapibus odio, eu gravida felis'
                           'blandit vel.Vivamus feugiat auctor lorem non eleifend.'
                           'Nam eu pellentesque est, vitae interdum nisi.',
            'picture': '/uploads/photo2.jpg',
            'sid': 'bace070115e3514497c547487d543032',
        })


if __name__ == '__main__':
    unittest.main()



