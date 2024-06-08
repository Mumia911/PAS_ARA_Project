from DB_requests import DB_requests
from DB_connection import DB_connection
from userLogin import UserLogin
from user import User
from Application import Application

if __name__ == "__main__":

# tworzenie instancji użytkownika
    user = User(1, "example_user", "user@example.com", True, "password", False)
# logowanie użytkownika
    login_manager = UserLogin()
    print(login_manager.login(user))

# sprawdzenie stanu zalogowania
    print("Is user logged in?", user.is_logged())

# dane do połączenia z bazą danych
    APIkey = "your_api_key"
    username = "your_username"
    password = "your_password"

# tworzenie instancji połączenia z bazą danych
    db_connection = DB_connection(APIkey, username, password)

# ustanowienie połączenia z bazą danych
    if db_connection.connection(APIkey, username, password):
        Application.add_entry(1, user)
        print("Entry added to the database.")
    else:
        print("Failed to establish connection to the database.")

# wylogowanie użytkownika
    print(login_manager.logout(user))

# sprawdzenie stanu zalogowania po wylogowaniu
    print("Is user logged in?", user.is_logged())


