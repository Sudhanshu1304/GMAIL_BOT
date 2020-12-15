from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

path= "D:/User/Desktop/MY APPS/Gmail_Bot/Email.txt"  #"Enter the PATH TO STORE THE EMAIL IN "


def From(email):

    try:
        file = open(path, 'r')
        content = file.read()

        content = content.split('\n')

        if email not in content:
            file.close()
            file = open(path, 'a')
            file.write(email + "\n")
        file.close()

    except:
        file = open(path, 'a')
        file.write(email + "\n")
        file.close()


def Options():

    global content, opt
    global gmail_user, gmail_password

    try:

        file = open(path, 'r')
        content = file.read()
        content = content.split('\n')

        c = 0
        for i in range(len(content)):
            if len(content[i]) != 0 and content[i]!='-1':
                print('\n', ' ', c, ' : ', content[i])
                c = c + 1

        file.close()

        print('\n', c, " : OTHER ")
        opt = int(input("\nChoice : "))

        if opt != (c):
            gmail_user = content[opt]

        else:
            gmail_user = input("\nEnter Your Email : ")
            From(gmail_user)

    except:

        gmail_user = input("\nEnter Your Email : ")
        From(gmail_user)


Options()

msgg = MIMEMultipart()

msgg['From'] =gmail_user


global content, opt

l = 0
inp = 0

iter = int(input("\nNo of Times : "))
gmail_password = input('\nEnter Password : ')
sent_from = gmail_user

TOO=[]
TO='initializing  TO'
while(TO!='-1'):
    TO = input("\nEmail TO (enter \'-1\' to exit ): ")
    if(TO!="-1"):
        TOO.append(TO)
        From(TO)

print('\nEnter Message  Body :  ')

lines = []
while True:
    line = input()
    if line:
        lines.append("\n")
        lines.append(line)
    else:
        break

text = ''.join(lines)

print("\n1. Subject Random Number\n2. EDIT \n")
o = int(input('Enter Your Choice : '))

if o == 2:
    subject = input("\nEnter SUBJECT : ")
else:
    subject = '#$$*{}$$%'.format(random
                                 .randint(100000000, 99999999999))

msgg['Subject']=subject

for i in range(iter):

    for to in TOO:
        print('TOO IS : ',to)
        msgg['To'] = to
        body = text
        body = MIMEText(body)
        msgg.attach(body)

        text = msgg.as_string()
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to,text)
            server.close()

            print('\nEmail sent!')
        except:
            print('Something went wrong...')