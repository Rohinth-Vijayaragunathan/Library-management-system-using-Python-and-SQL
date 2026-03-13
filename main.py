from admin.admin_auth import create_admin, admin_login
from user.user_auth import user_login, register_user

while True:

    print("\n1.create admin")
    print("2.Admin Login")
    print("3.User Login")
    print("4.Register user")
    print("5.Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number")
        continue

    if choice == 1:
        create_admin()

    if choice == 2:
        admin_login()

    elif choice == 3:
        user_login()

    elif choice == 4:
        register_user()

    elif choice == 5:
        print("Exiting program")
        break
