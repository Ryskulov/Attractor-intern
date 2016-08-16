import unittest
from database import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_create_login(self):
        self.user.create_login('randomir', 'password', 'Name', 'chingizkg@gmail.com')
        self.assertEqual(self.user.username[1], 'randomir')

    def test_create_password(self):
        self.user.create_login('randomir', 'password', 'Name', 'chingizkg@gmail.com')
        self.assertEqual(self.user.password[1], 'password')

if __name__ == '__main__':
    unittest.main()



