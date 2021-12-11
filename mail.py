import smtplib # importing the smtp module for smtp mail services
from email.message import EmailMessage # importing EmailMessage class from email.message module to create email messages

# Function to send email that gets the email list, subject and msg
def sendingMail(emails, sub, msgg):
    gmail_user = 'user' # the user for the smtp server
    gmail_password = 'pass' # the password for the smtp server


    msg = EmailMessage() # creating msg object
    msg.set_content(msgg) # setting the content of the msg object
    msg['Subject'] = sub # setting the subject of the msg object
    msg['From'] = gmail_user # setting the from of the msg object
    msg['To'] = emails # setting the to of the msg object

    try: # try to send the email
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # connecting to the smtp server
        smtp_server.ehlo() # saying hello to the smtp server, to see if everything is okay
        smtp_server.login(gmail_user, gmail_password) # login to the smtp server
        smtp_server.send_message(msg) # sending the msg
        smtp_server.close() # close the connection
        print ("Email sent successfully!") # print the success message just to make sure + debugging
    except Exception as ex: # if there is an error
        print ("Something went wrong….",ex) # print that something went wrong and the error what is wrong