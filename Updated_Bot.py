from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email.mime.text import MIMEText
import smtplib
import random

path= "Email.txt"  #"Enter the PATH TO STORE THE EMAIL IN "


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

iter = 1 #int(input("\nNo of Times : "))

gmail_password = input('\nEnter Password : ')
sent_from = gmail_user


op=int(input('Send Files (1/0) : '))

if op==1:
    

    lines1 = []
    while True:
        line1 = input('Enter File : ')
        if line1:
            lines1.append(line1)
        else:
            break

    f=input("Enter File : ")


TOO=[]
TO='initializing  TO'

while(TO!='-1'):
    TO = input("\nEmail TO (enter \'-1\' to exit ): ")
    if(TO!="-1"):
        TOO.append(TO)
        From(TO)


opt=int(input('Enter Message (1/0) : '))
if opt==1:
    print('\nEnter Message  Body (Enter twice to exit! ) :  ')

    lines = []
    while True:
        line = input()
        if line:
            lines.append("\n")
            lines.append(line)
        else:
            break

    text = ''.join(lines)
else:
    text="."


subject = input("\nEnter SUBJECT : ")

msgg['Subject']=subject

for i in range(iter):

    for to in TOO:
        
        for f in lines1:
            f1=f.split('\\')
            f="/".join(f1)
            try:
                with open(f, "rb") as fil:
                    
                    part = MIMEApplication(
                        fil.read(),
                        Name=basename(f)
                    )
            except:
                s=''
                for e in f:
                    if e!='"' and e!= "'" and e!='\n':
                        s=s+e
                f=s
               
                with open(f, "rb") as fil:
                    
                    part = MIMEApplication(
                        fil.read(),
                        Name=basename(f)
                    )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msgg.attach(part)
        
        
        
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

