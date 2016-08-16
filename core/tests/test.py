import unittest
#from db.database import User
from db.database import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    # def tearDown(self):
    #     del self.user

    def test_create_user(self):
        self.user.create_login('randomir', 'password', 'Name', 'chingizkg@gmail.com')
        self.assertAlmostEquals(self.user.username[1], 'randomir')


if __name__ == '__main__':
    unittest.main()



