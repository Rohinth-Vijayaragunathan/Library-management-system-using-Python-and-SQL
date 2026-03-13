from config.db_config import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Admin(
admin_id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(30),
password VARCHAR(30)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS User(
user_id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(30),
password VARCHAR(30)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
book_id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(30),
author VARCHAR(30),
quantity INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Issued_books(
issue_id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT,
book_id INT,
issue_date DATE,
return_date DATE,
fine INT DEFAULT 0
)
""")

connection.commit()
print("All tables created successfully")
