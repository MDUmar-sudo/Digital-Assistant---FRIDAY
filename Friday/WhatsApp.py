import pywhatkit as kit
from datetime import datetime

def recipient(data):
    print(data)
    number = ""
    if data == " faridi":
        number = "+918285879667"
    elif data == " shrijan":
        number = "+917979904265"
    elif data == " mama":
        number = "+919038711753"
    elif data == " anil":
        number = "+919106305700"
    else:
        print("wrong recipient")
        exit()
    return number


def message(number, message):
    h = int(datetime.now().hour)
    m = int(datetime.now().minute)+2
    kit.sendwhatmsg(number,message,h,m)