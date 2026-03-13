from config.db_config import get_connection
from datetime import date

connection = get_connection()
cursor = connection.cursor()

def view_book():

    cursor.execute("SELECT * FROM Books")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def issue_book(user_id):

    book_id = int(input("Enter book id: "))

    cursor.execute(
        "SELECT quantity FROM Books WHERE book_id=%s",
        (book_id,)
    )

    qty = cursor.fetchone()

    if qty and qty[0] > 0:

        cursor.execute(
            "INSERT INTO Issued_books(user_id,book_id,issue_date) VALUES(%s,%s,%s)",
            (user_id,book_id,date.today())
        )

        cursor.execute(
            "UPDATE Books SET quantity=quantity-1 WHERE book_id=%s",
            (book_id,)
        )

        connection.commit()

        print("Book issued successfully")

    else:
        print("Book not available")

def user_menu(user_id):

    while True:

        print("\n1.View Books")
        print("2.Issue Book")
        print("3.Logout")

        choice = int(input("Enter choice: "))

        if choice == 1:
            view_book()

        elif choice == 2:
            issue_book(user_id)

        else:
            print("User logout")
            break
