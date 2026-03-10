from admin.admin_auth import admin_login
from user.user_auth import user_login

while True:

    print("\n1.Admin Login")
    print("2.User Login")
    print("3.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        admin_login()

    elif choice == 2:
        user_login()

    else:
        print("Exiting program")
        break