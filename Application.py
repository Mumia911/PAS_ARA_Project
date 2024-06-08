from DB_requests import DB_requests
from DB_connection import DB_connection

class Application:
    def __init__(self, entryID):
        super().__init__(entryID)

    def add_entry(self):
        if(DB_connection.connection == True):
            print("Application added to repo")

    def modify_entry(self):
        if(DB_connection.connection == True):
            print("Application modified in repo")

    def delete_entry(self):
        if(DB_connection.connection == True):
            print("Application removed from repo")
    def search_entry(self):
        if(DB_connection.connection == True):
            print("Serching for application in repo")