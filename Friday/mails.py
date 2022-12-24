import smtplib
from email.message import EmailMessage

def recipient(data):
    print(data)
    to = ""
    if data == " umar":
        to = "risingsheikh@gmail.com"
    elif data == " faridi":
        to = "Khanaarhan18@gmail.com"
    elif data == " sonu":
        to = "sonu84957@gmail.com"
    elif data == " gamma":
        to = "grays9913@gmail.com"
    elif data == " sanjib":
        to = "callmesanjib@rediff.com"
    elif data ==" md":
        to = "mdumarmca2022@bpibs.in"
    else:
        print("wrong recipient")
        exit()
    return to

def sendEmail(to, content):
    msg = EmailMessage()
    msg['Subject'] = "Please read the mail !!"
    msg['From'] = "techw6480@gmail.com"
    msg['To'] = to
    msg.set_content(content)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login("techw6480@gmail.com", "technical1405")
    server.send_message(msg) # sendmail() method if not using EmailMessage() method
    server.quit()


