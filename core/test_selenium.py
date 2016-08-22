import unittest
from selenium import webdriver
from db.database import DataAccessLayer
import uuid
import subprocess


SID = str(uuid.uuid4().hex)


class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.pid_server = subprocess.Popen('python server.py', shell=True)
        self.dal = DataAccessLayer()
        self.driver = webdriver.Firefox()

    def test_sign_up_user(self):
        self.driver.get('http://localhost:8080/signup/')
        username = self.driver.find_element_by_name('username')
        username.send_keys('randomir')
        password = self.driver.find_element_by_name('password')
        password.send_keys('global24')
        email = self.driver.find_element_by_name('email')
        email.send_keys('chingiz@gmail.com')
        first_name = self.driver.find_element_by_name('first_name')
        first_name.send_keys('Chingiz')
        self.dal.create_user(
            username=username.get_attribute('value'),
            password=password.get_attribute('value'),
            email=email.get_attribute('value'),
            first_name=first_name.get_attribute('value'),
            sid=SID
        )
        register_button = self.driver.find_element_by_class_name('form__btn')
        register_button.click()

        username = self.driver.find_element_by_name('username')
        username.send_keys('randomir')
        password = self.driver.find_element_by_name('password')
        password.send_keys('global24')
        login_button = self.driver.find_element_by_class_name('form__btn')
        login_button.click()


    def tearDown(self):
        self.driver.close()
        self.pid_server.kill()


if __name__ == "__main__":
    unittest.main()









# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.db = DataAccessLayer()
#
#     def test_authenticated_user(self):
#
#
#
#         btn_go = self.driver.find_element_by_css_selector('a[href="/admin/"]')
#         btn_go.click()

#         btn_login = self.driver.find_element_by_css_selector('input[type="submit"]')
#         btn_login.click()
#         # def tearDown(self):
#         #     self.driver.close()
