import unittest
from db.database import DataAccessLayer


class TestUser(unittest.TestCase):

    def setUp(self):
        self.dal = DataAccessLayer()

    def tearDown(self):
        del self.dal

    def test_user_signup_login_more_2_characters(self):
        self.dal.create_user(username='randomir', password='password',
                             email='chingiz@gmail.com', sid='asd3421dasfsdfsfd',
                             first_name='Chingiz')
        self.assertEqual(self.dal.user.dict_users[2]['username'], 'randomir')

    def test_user_sign_in_true(self):
        self.assertTrue(self.dal.check_user_is_exist('admin', 'admin'))

    def test_user_sign_in_false(self):
        self.assertFalse(self.dal.check_user_is_exist('otherlogin', 'badpassword'))

    def test_user_signup_login_less_2_characters(self):
        self.assertFalse(self.dal.create_user(
            username='r', password='password',
            email='chingiz@gmail.com', sid='asd3421dasfsdfsfd',
            first_name='Chingiz'))

    def test_user_signup_login_is_empty(self):
        self.assertFalse(self.dal.create_user(
            username='', password='password',
            email='chingiz@gmail.com', sid='asd3421dasfsdfsfd',
            first_name='Chingiz'))

if __name__ == '__main__':
    unittest.main()



