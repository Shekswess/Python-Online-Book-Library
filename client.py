import requests # import requests library for client side to communicate with server via API
import getpass # import getpass library to hide password
import os # import os library to use os commands to clear terminal

# clear the console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# main menu options (printing)
def mainMenuOption():
    print('Please choose one of the following options:')
    print('1. List all books')
    print('2. Search for a book by id')
    print('3. Add a book')
    print('4. Delete a book by id')
    print('5. Update a book by id')
    print('6. Logout')
    print()

# if logged in, show the main menu and work with the following options
def mainMenu():
    while True:
        mainMenuOption()
        cmd = int(input('Please enter your choice for what operation you want: '))
        if cmd == 1:
            listBooks()
        elif cmd == 2:
            searchBookID()
        elif cmd == 3:
            addBook()
        elif cmd == 4:
            deleteBook()
        elif cmd == 5:
            updateBook()
        elif cmd == 6:
            clearConsole()
            break
        else:
            print('Please enter a valid choice !')

# if logged in, list the books function
def listBooks():
    clearConsole()
    responce = requests.get("http://127.0.0.1:8000/books") # send a get request to the server to get the list of books
    if responce.status_code == 200: # 200 == OK status code
        books = responce.json() # get the list of books from the server
        for b in books:
            print(b['id'], b['name'], b['author'], b['genre'], b['rating'])
            print()
    else:
        print('Can not access the server !')
        print(f'The error is {responce.status_code} !') # print the error code
        print()

# if logged in, search a book by id and show it function
def searchBookID():
    clearConsole()
    print('Please enter the id of the book you want to search:')
    id = int(input())
    print()
    responce = requests.get(f"http://127.0.0.1:8000/books/{id}") # send a get request to the server to get the book by id
    if responce.status_code == 200: # 200 == OK status code
        book = responce.json() # get the book from the server
        print(book['id'], book['name'], book['author'], book['genre'], book['rating'])
        print()
    else:
        print('Can not access the server !')
        print(f'The error is {responce.status_code} !')  # print the error code
        print()

# if logged in, add a book  function
def addBook():
    clearConsole()
    print('Please enter the name of the book:')
    name = input()
    print()
    print('Please enter the author of the book:')
    author = input()
    print()
    print('Please enter the genre of the book:')
    genre = input()
    print()
    print('Please enter the rating of the book:')
    rating = float(input())
    print()
    responce = requests.post(f"http://127.0.0.1:8000/books/{name}&{author}&{genre}&{rating}")
    if responce.status_code == 200:
        print('Add book successful !')
        print()
    else:
        print('Can not access the server !')
        print(f'The error is {responce.status_code} !')  # print the error code
        print()

# if logged in, delete a book by id function
def deleteBook():
    clearConsole()
    print('Please enter the id of the book you want to delete:')
    id = int(input())
    print()
    responce = requests.delete(f"http://127.0.0.1:8000/books/{id}")
    if responce.status_code == 200:
        print('Delete successful !')
        print()
    else:
        print('Can not access the server !')
        print(f'The error is {responce.status_code} !')  # print the error code
        print()

# if logged in, update a book by id function
def updateBook():
    clearConsole()
    print('Please enter the id of the book you want to update: ')
    id = int(input())
    print()
    print('Please enter the name of the book:')
    name = input()
    print()
    print('Please enter the author of the book:')
    author = input()
    print()
    print('Please enter the genre of the book:')
    genre = input()
    print()
    print('Please enter the rating of the book:')
    rating = float(input())
    print()
    responce = requests.put(f"http://127.0.0.1:8000/books/{id}&{name}&{author}&{genre}&{rating}")
    if responce.status_code == 200:
        print('Update successful !')
        print()
    else:
        print('Can not access the server !')
        print(f'The error is {responce.status_code} !')  # print the error code
        print()

# login menu operations
def loginMenuOption():
    print('Welcome to the python online book library !')
    print('Please choose one of the following options:')
    print('1. Login')
    print('2. Register')
    print('3. Exit')
    print()

# show the login menu and work with the following options
def loginMenu():
    while True:
        loginMenuOption()
        cmd = int(input('Please enter your choice: '))
        if cmd == 1:
            if login():
                mainMenu()
                print()
            else:
                print('Login failed !')
                print('You have entered wrong credentials !')
                print()
                continue
        elif cmd == 2:
            register()
        elif cmd == 3:
            break
        else:
            print('Please enter a valid choice !')

# login option
def login():
    clearConsole()
    print('Please enter your username:')
    username = input()
    print()
    print('Please enter your password:')
    password = getpass.getpass() # hide the input in the terminal
    print()
    responce = requests.get("http://127.0.0.1:8000/accounts") # send a get request to the server to get all the accounts
    if responce.status_code == 200: # 200 == OK status code
        loginList = responce.json() # get the list of accounts from the server
        for l in loginList:
            if l['name'] == username and l['password'] == password: # check if the username and password are correct
                print('Login successful !')
                print()
                return True
                break # if we don't break the loop, the program will continue to check the next account
    else:
        print('Login failed can not access the server !')
        print()
        return False

# register option
def register():
    clearConsole()
    print('Please enter your username:')
    username = input()
    print()
    print('Please enter your password:')
    password = getpass.getpass() # hide the input in the terminal
    print()
    print('Please enter your email:')
    email = input()
    print()
    emailresponce = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params = {'email': email}) # send a get request to an already build API that checks if the email is valid
    status = emailresponce.json()['status'] # get the status of the email
    if status == 'valid': # if the email is valid
        responce = requests.post(f"http://127.0.0.1:8000/accounts/{username}&{password}&{email}") # send a post request to the server to add the account
        if responce.status_code == 200: # 200 == OK status code
            print('Register successful !')
            print()
        else:
            print('Register failed !')
            print(f'The error is {responce.status_code} !')  # print the error code
            print()
    elif status == 'invalid':
        print('Invalid email !')
        print()
    else:
        print('Unknown email !')

loginMenu() # starting the program

