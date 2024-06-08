class User:
    def __init__(self, id, login, email, is_admin, password, logged):
        self._id = id
        self._login = login
        self._email = email
        self._is_admin = is_admin
        self._password = password
        self._logged = logged

    def get_id(self):
        return self._id

    def get_login(self):
        return self._login

    def get_email(self):
        return self._email

    def is_admin(self):
        return self._is_admin

    def get_password(self):
        return self._password

    def is_logged(self):
        return self._logged

    def set_id(self, id):
        self._id = id

    def set_login(self, login):
        self._login = login

    def set_email(self, email):
        self._email = email

    def set_is_admin(self, is_admin):
        self._is_admin = is_admin

    def set_password(self, password):
        self._password = password

    def set_logged(self, logged):
        self._logged = logged

