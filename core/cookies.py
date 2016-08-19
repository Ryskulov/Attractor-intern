class Cookie:
    cookie_dict = {}

    def create_cookie(self, cookie_key, cookie_value):
        self.cookie_dict[cookie_key] = cookie_value

    def get_cookie(self, cookie_key, cookie_value):
        self.cookie_dict[cookie_key] = cookie_value

    def __get__(self):
        return self.cookie_dict
