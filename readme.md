#  Library Management System

A simple **Library Management System** built using **Python and MySQL**.  
This project allows an **Admin** to manage books and **Users** to view, issue, and return books.  
The system also calculates fines for late returns.

---

##  Features

### Admin
- Add new books
- View all books
- Search books
- Update book details
- Delete books

### User
- View available books
- Issue books
- Return books
- Automatic fine calculation for late returns

---

##  Project Structure

library_management/
│
├── admin/
│ ├── admin_auth.py
│ └── admin_operations.py
│
├── user/
│ ├── user_auth.py
│ └── user_operations.py
│
├── config/
│ └── db_config.py
│
├── database/
│ └── create_tables.py
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

##  Requirements

To run this project, you need:

- Python 3.8 or higher
- MySQL Server
- MySQL Workbench (optional)
- VS Code or any Python IDE
- pip (Python package manager)

### Python Libraries

- pymysql
- python-dotenv

---

##  Technologies Used

- **Python** – Core programming language used to develop the application.
- **MySQL** – Database used to store book and user information.
- **PyMySQL** – Used to connect Python with the MySQL database.
- **python-dotenv** – Used to securely manage database credentials.
- **SQL** – Used for database queries and table management.

---

##  Installation

### 1 Clone the repository

```bash
git clone https://github.com/yourusername/library-management-system.git

## Project Setup Guide
```
2. Navigate to the Project Folder

cd library-management-system
```
3. Install dependencies
pip install -r requirements.txt


4. Create a .env file
Add the following configuration:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=library_DB

```
5. Create database in MySQL
CREATE DATABASE library_DB;

6. Run the table creation file
python database/create_tables.py

7. 7 Run the project
python main.py