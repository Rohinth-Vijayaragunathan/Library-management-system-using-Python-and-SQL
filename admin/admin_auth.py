from config.db_config import get_connection
from admin.admin_operations import admin_menu

connection = get_connection()
cursor = connection.cursor()

def admin_login():
    u = input("Enter username: ")
    p = input("Enter password: ")

    cursor.execute(
        "SELECT * FROM Admin WHERE username=%s AND password=%s",
        (u,p)
    )

    if cursor.fetchone():
        print("Admin login successful")
        admin_menu()
    else:
        print("Invalid admin login")
