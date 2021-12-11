import sqlite3 # importing sqlite3 for the database

# Creating the tables
def createTableAccountsBooks():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    table_cmd = f'CREATE TABLE IF NOT EXISTS books(name_book TEXT, name_author TEXT, genre TEXT, rating REAL)'

    cursor.execute(table_cmd)

    table_cmd = f'CREATE TABLE IF NOT EXISTS accounts(user TEXT, password TEXT, email TEXT)'

    cursor.execute(table_cmd)

    conn.commit()

    conn.close()

# Inserting data into the tables
def insertTableAccountsBooks():

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    books = [('Fifty Shades of Grey', 'E.L. James', 'Romance', 4.1), ('Twilight', 'Stephenie Meyer', 'Romance', 4.4),
         ('The Notebook', 'Nicholas Sparks', 'Romance', 3.9), ('John Adams', 'David McCullough', 'History', 4.0),
         ('The Diary of a Young Girl', 'Anne Frank', 'History', 4.1), ('1776', 'David McCullough', 'History', 3.8),
         ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 4.4), ('1984', 'George Orwell', 'Fiction', 4.3),
         ('The Lord of the Rings', ' J.R.R. Tolkien', 'Fiction', 4.9), ('Fahrenheit 451', 'Ray Bradbury', 'Fiction', 3.9),
         ('A Game of Thrones', 'George R.R. Martin', 'Fiction', 4.4), ('The Hobbit, or There and Back Again', 'J.R.R. Tolkien', 'Fiction', 4.8),
         ('Clean Code', 'Robert Cecil', 'Computer Science', 4.5), ('Code Complete', 'Steve McConnell', 'Computer Science', 4.1),
         ('Cracking the Coding Interview', 'Gayle Laakmann McDowell', 'Computer Science', 4.8), ('Coders at Work', 'Peter Seibel', 'Computer Science', 3.7),
         ('The 4-Hour Workweek', 'Tim Ferriss', 'Business', 3.9), ('The Lean Startup', 'Eric Ries', 'Business', 4.1),
         ('Steve Jobs', 'Walter Isaacson', 'Biography', 4.2), ('Long Walk to Freedom', 'Nelson Mandela', 'Biography', 4.6)]

    cursor.executemany('INSERT INTO books VALUES (?,?,?,?)', books)

    accounts = [('admin', 'admin', 'real mail address'), ('john', 'john123!', 'john.smith@yahoo.com')]

    cursor.executemany('INSERT INTO accounts VALUES (?,?,?)', accounts)

    conn.commit()

    conn.close()

# Printing the data from the tables (just for testing)
def printTableAccountsBooks():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    table = f"SELECT rowid, * from books"

    cursor.execute(table)

    books = cursor.fetchall()

    for book in books:
        print(book)
        print()
    print("Done !")

    table = f"SELECT rowid, * from accounts"

    cursor.execute(table)

    accounts = cursor.fetchall()

    for account in accounts:
        print(account)
        print()
    print("Done !")

    conn.commit()

    conn.close()

# Testing functions for the database
createTableAccountsBooks()
insertTableAccountsBooks()
printTableAccountsBooks()