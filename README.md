# PYTHON ONLINE BOOK LIBRARY

-This is a project that is made for my Network Programming course but it's also a nice portfolio project

-The main goal of this project is to learn and implement some concept of basic python, advanced python,
network programming concepts, building Rest API, working with Rest API, working with requests, working
with database, working with SMTP, etc.

-In this project I work with many python libraries and modules: SMTP, FastAPI, sqlite3, OS, EmailMessage, etc.

-This project can be upgraded with more work on the API in near future 

-The project is consisting of frontend and backend part.

-The frontend part is consisting of client.py

-The backend part is consisting of database.py, mail.py, main.py

-Before working with the project you need to modify the mail.py code, where you will enter your smtp server account on line 6 and 7. Also you need to change the url for requests in the client.py code if you host your API on the Internet. You will also need to create the database by running the database.py code.

-Helpful documentation:
    ### https://docs.python-requests.org/en/latest/ - Requests
    ### https://docs.python.org/3/library/sqlite3.html - sqlite3
    ### https://fastapi.tiangolo.com/ - FastAPI


# Working with the project

-You need to have installed python 3.9 or higher version 

### Install dependencies on Client Side

```bash
pip install requests
```

### Install dependencies on Server Side

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

### Run on Client Side

```bash
python3 client.py
```

### Run on Server Side

```bash
python3 database.py 
uvicorn main:app --reload 
```
