from config.db_config import get_connection

connection = get_connection()
cursor = connection.cursor()

def add_book(title,author,quantity):
    sql = "INSERT INTO Books(title,author,quantity) VALUES(%s,%s,%s)"
    cursor.execute(sql,(title,author,quantity))
    connection.commit()
    print("Book added successfully")

def view_book():
    cursor.execute("SELECT * FROM Books")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def delete_book(book_id):
    cursor.execute("DELETE FROM Books WHERE book_id=%s",(book_id,))
    connection.commit()
    print("Book deleted")

def admin_menu():

    while True:

        print("\n1.Add Book")
        print("2.View Books")
        print("3.Delete Book")
        print("4.Logout")

        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Title: ")
            author = input("Author: ")
            quantity = int(input("Quantity: "))
            add_book(title,author,quantity)

        elif choice == 2:
            view_book()

        elif choice == 3:
            book_id = int(input("Book id: "))
            delete_book(book_id)

        else:
            print("Admin logout")
            break
