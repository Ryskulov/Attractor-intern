import unittest
#from db.database import User
from db.database import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_create(self):
        result = self.user.CreateLogin('randomir', 'password', 'Name', 'chingizkg@gmail.com')
        self.assertEqual(result, 'randomir', 'password', 'Name', 'chingizkg@gmail.com')


if __name__ == '__main__':
    unittest.main()



