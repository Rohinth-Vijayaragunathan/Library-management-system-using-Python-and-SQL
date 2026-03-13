from config.db_config import get_connection
from admin.admin_operations import admin_menu

connection = get_connection()
cursor = connection.cursor()

def create_admin():
    u = input("Enter username: ")
    p = input("Enter password: ")

    sql = "INSERT INTO Admin (username, password) VALUES(%s, %s)"
    cursor.execute(sql, (u, p))
    connection.commit()
    print("Admin created successfully")
    
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

