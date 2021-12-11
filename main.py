from fastapi import FastAPI # importing FastAPI for the REST API
import sqlite3 # importing sqlite3 for the database
from mail import sendingMail # importing sendingMail function from the mail.py file

app = FastAPI() # Starting the API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # DATABASE COMMUNICATION PART OF THE APP # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Getting all the books from the database
def getBooks():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    table = f'SELECT rowid, * from books ORDER BY rowid'

    cursor.execute(table)

    books = cursor.fetchall()

    booksDict = []
    for book in books:
        booksDict.append({"id": book[0], "name": book[1], "author": book[2], "genre": book[3], "rating": book[4]})

    conn.commit()

    conn.close()

    return booksDict

# Getting a book from the database by id
def getBookByID(id):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT rowid, * from books WHERE rowid = :number', {"number": id})

    book = cursor.fetchall()

    book_return = {"id": book[0][0], "name": book[0][1], "author": book[0][2], "genre": book[0][3], "rating": book[0][4]}

    conn.commit()

    conn.close()

    return book_return

# Getting the accounts from the database
def getAccounts():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    table = f'SELECT rowid, * from accounts ORDER BY rowid'

    cursor.execute(table)

    accounts = cursor.fetchall()

    accountsDict = []
    for account in accounts:
        accountsDict.append({"id": account[0], "name": account[1], "password": account[2], "email": account[3]})

    conn.commit()

    conn.close()

    return accountsDict

# Getting an account from the database by id
def getAccountsById(id):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT rowid, * from accounts WHERE rowid = :number', {"number": id})

    account = cursor.fetchall()

    account_return = {"id": account[0][0], "name": account[0][1], "password": account[0][2], "email": account[0][3]}

    conn.commit()

    conn.close()

    return account_return

# Getting the list of the mail addresses where we need to send a msg if there is a change in the library
def getEmails():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    table = 'SELECT email from accounts ORDER BY rowid'

    cursor.execute(table)

    emails = cursor.fetchall()
    mails=[]

    for email in emails:
        mails.append(email[0])

    conn.commit()

    conn.close()

    return mails

# Adding an account to the library function(users)
def postAccount(name, password, email):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    account = [(name, password, email)]

    cursor.executemany(f"INSERT INTO accounts VALUES (?,?,?)", account)

    conn.commit()

    conn.close()

# Adding a book to the library (database)
def postBook(name, author, genre, rating):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    book = [(name, author, genre, rating)]

    cursor.executemany(f"INSERT INTO books VALUES (?,?,?,?)", book)

    conn.commit()

    conn.close()

# Deleting a book from the library(database)
def deleteBookById(id):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM books WHERE rowid = {id}")

    conn.commit()

    conn.close()

# Updating a book in the library(database)
def updateBookById(id, name, author, genre, rating):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(
        f"UPDATE books SET name_book = '{name}', name_author = '{author}', genre = '{genre}', rating = '{rating}' WHERE rowid = {id}")

    conn.commit()

    conn.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # API PART OF THE APP # # # # # # # # # # # # # # # # ## # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# root and /books get requests, returns the list of books in the library
@app.get("/")
@app.get("/books")
def read_books():
    return getBooks()

# /books/<id> get request, returns a book by id
@app.get("/books/{id}")
def read_book_by_id(id: int):
    return getBookByID(id)

# /accounts get request, returns the list of accounts in the library
@app.get("/accounts")
def read_accounts():
    return getAccounts()

# /accounts/<id> get request, returns an account by id
@app.get("/accounts/{id}")
def read_account(id):
    return getAccountsById(id)

# /book/{name}/{author}/{genre}/{rating} post request, adds a book to the library
@app.post("/books/{name}&{author}&{genre}&{rating}")
def create_book(name: str, author: str, genre:str, rating:float):
    emails = getEmails()
    sub = "New book is added to the library !"
    msg = f'New book is added to the library ! '\
          f'The name of the book is {name} by the author {author}.' \
          f' The genre of the book is {genre} and it has rating {rating} !'
    postBook(name, author, genre, rating)
    sendingMail(emails, sub, msg)

# /accounts/{name}/{password}/{email} post request, adds an account to the database
@app.post("/accounts/{name}&{password}&{email}")
def create_account(name:str, password:str, email:str):
    postAccount(name, password, email)

# /books/{id} delete request, deletes a book from the library
@app.delete("/books/{id}")
def delete_book(id:int):
    emails = getEmails()
    sub = "Book is deleted from the library !"
    msg = f'Book is deleted from the library ! '
    deleteBookById(id)
    sendingMail(emails, sub, msg)

# /books/{id} put request, updates a book in the library
@app.put("/books/{id}&{name}&{author}&{genre}&{rating}")
def update_book(id:int, name:str, author:str, genre:str, rating:float):
    emails = getEmails()
    sub = "Book is updated in the library !"
    msg = f'Book is updated in the library ! '\
          f'The name of the book is {name} by the author {author}.' \
          f' The genre of the book is {genre} and it has rating {rating} !'
    updateBookById(id, name, author, genre, rating)
    sendingMail(emails, sub, msg)

