import uuid

host_url = 'http://127.0.0.1:8080'
SID = str(uuid.uuid4().hex)

site_mapping = {
    "registration": {
        "url": host_url + "/signup/",
        "username": "//input[@name='username']",
        "password": "//input[@name='password']",
        "email": "//input[@name='email']",
        "first_name": "//input[@name='first_name']",
        "sid": SID,
        "signup_button": "//button[@type='submit']",
    },
    "authorization": {
        "url": host_url + "/login/",
        "username": "//input[@name='username']",
        "password": "//input[@name='password']",
        "login_button": "//button[@type='submit']",
    },
}