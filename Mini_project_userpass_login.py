# Creating a login system.

from getpass import getpass
from passlib.hash import bcrypt


users = {}  # Username changed into password hash.

while True:
    choice = input("Would you like to login, register or leave?").strip().lower()  # Main question.
    if choice == "leave":
        print("Goodbye!")
        break  # End of leave command.
    elif choice == "register":
        username = input("Username: ").strip()
        if username in users:
            print("Username already registered")
            continue  # Go back to main menu.
        password = getpass("Password: ")  # Typing is hidden when typing password.
        users[username] = bcrypt.hash(password)
        print("Account created!")  # End of register command.
    elif choice == "login":
        username = input("Username: ").strip()
        password = getpass("Password: ")
        if username in users and bcrypt.verify(password, users[username]):
            print("Login successful")
        else:
            print("Login unsuccessful. Invalid Username or Password.")
    else:
        print("Please type 'login', 'register' or 'leave'.")






