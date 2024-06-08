from DB_requests import DB_requests
from DB_connection import DB_connection

class Module:
    def __init__(self, entryID):
        super().__init__(entryID)

    def add_entry(self):
        if(DB_connection.connection == True):
            print("Module added to repo")

    def modify_entry(self):
        if(DB_connection.connection == True):
            print("Module modified in repo")

    def delete_entry(self):
        if(DB_connection.connection == True):
            print("Module removed from repo")
    def search_entry(self):
        if(DB_connection.connection == True):
            print("Serching for module in repo")