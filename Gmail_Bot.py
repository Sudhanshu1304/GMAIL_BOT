import smtplib
import  random



def From(email):

    file=open('D:/User/Desktop/MY APPS/Gmail_Bot/Email.txt','a+')
    content = file.read()
    content = content.split('\n')

    if email not in content:
        file.write(email+"\n")
        file.close()


def Options():

    global content,opt
    global gmail_user, gmail_password

    try :

        file=open("D:/User/Desktop/MY APPS/Gmail_Bot/Email.txt",'r')
        content=file.read()
        content=content.split('\n')

        c=0
        for i in range(len(content)):
            if len(content[i])!=0 :
                print('\n',' ',c,' : ',content[i])
                c=c+1

        file.close()

        print('\n',c," : OTHER ")
        opt=int(input("\nChoice : "))
        if opt !=(c):
            gmail_user = content[opt]
        else:
            gmail_user = input("\nEnter Your Email : ")
            From(gmail_user)

    except:

        gmail_user=input("\nEnter Your Email : ")
        From(gmail_user)




Options()

global content,opt

l=0
inp=0

iter=int(input("\nNo of Times : "))
gmail_password = input('\nEnter Password : ')
sent_from = gmail_user
TO=input("\nEmail TO : ")


msg=input("\nEnter The message  : ")

for _ in range(iter):



    to = [ TO ]

    subject = '{}'.format(random
                          .randint(100000000,99999999999))

    body=msg

    email_text = """From: %s
    To: %s\n
    Subject: %s\n

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('\nEmail sent!')
    except:
        print ('Something went wrong...')

