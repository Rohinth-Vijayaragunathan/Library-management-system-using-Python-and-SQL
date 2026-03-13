from config.db_config import get_connection
from user.user_operations import user_menu

connection = get_connection()
cursor = connection.cursor()

def register_user():
    username = input("enter the username: ")
    password = input("enter the password: ")

    sql = "INSERT INTO User(username, password) values (%s, %s)"
    cursor.execute(sql , (username, password))
    connection.commit()
    print("user created successfully")

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

