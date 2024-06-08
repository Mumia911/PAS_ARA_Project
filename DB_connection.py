class DB_connection:
    def __init__(self, APIkey, username, password):
        self.APIkey = APIkey
        self.username = username
        self.password = password

    def connection(self, APIkey, username, password):
        print("Connected to DB")
        return True

