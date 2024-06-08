from DB_requests import DB_requests
from DB_connection import DB_connection
from user import User


class Application:
    def __init__(self, entryID, user):
        self.user = user
        super().__init__(entryID)

    def add_entry(self, user):
        if DB_connection.connection == True and user.is_admin():
            print("Application added to repo")
        else:
            print("Operation failure")

    def modify_entry(self, user):
        if DB_connection.connection == True and user.is_admin() == True:
            print("Application modified in repo")
        else:
            print("Operation failure")

    def delete_entry(self, user):
        if DB_connection.connection == True and user.is_admin() == True:
            print("Application added to repo")
        else:
            print("Operation failure")

    def search_entry(self):
        if DB_connection.connection == True:
            print("Serching for application in repo")
