class Authentication:
    def __init__(self, user, authentication_method):
        self.user = user
        self.authentication_method = authentication_method

    def user_authentication(self):
        print("Authentication successful")
        return True

from userLogin import UserLogin