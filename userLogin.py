class UserLogin:
    def __init__(self):
        pass

    def login(self, user):
        if Authentication.user_authentication(user):
            user.set_logged(True)
            return "Login successful"
        else:
            return "Invalid credentials"

    def logout(self, user):
        if user.is_logged():
            user.set_logged(False)
            return "Logout successful"
        else:
            return "User is not logged in"

from authentication import Authentication