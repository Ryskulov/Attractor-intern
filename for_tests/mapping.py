import uuid

host_url = 'http://localhost:8080'
SID = str(uuid.uuid4().hex)

site_mapping = {
    "registration": {
        "url": host_url + "/signup/",
        "username": "//input[@name='username']",
        "password": "//input[@name='password']",
        "email": "//input[@name='email']",
        "first_name": "//input[@name='last_name']",
        "sid": SID,
        "signup button": "//button[@class='form__btn']",
    },
    # "authorization": {
    #     "url": host_url + "/login/",
    #     "username": "//input[@id='username']",
    #     "password": "//input[@name='password']",
    #     "login button": "//button[@name='login']",
    #     "status message": "//div[@id='status']",
    # },
}