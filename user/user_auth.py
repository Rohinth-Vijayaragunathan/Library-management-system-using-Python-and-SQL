from config.db_config import get_connection
from user.user_operations import user_menu

connection = get_connection()
cursor = connection.cursor()

def user_login():

    u = input("Enter username: ")
    p = input("Enter password: ")

    cursor.execute(
        "SELECT * FROM User WHERE username=%s AND password=%s",
        (u,p)
    )

    user = cursor.fetchone()

    if user:
        print("User login successful")
        user_menu(user[0])
    else:
        print("Invalid login")
