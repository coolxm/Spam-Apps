import time
import requests
from fbchat import Client
from getpass import getpass
from fbchat.models import *
import keyboard

#log into messenger
username = str(input("Username: "))
pswd = str(getpass("pass: "))
client = Client(username, pswd)

time.sleep(10)

txt = open(input(), "r")


for word in txt:
    #formulate message
    msg = word
    print(msg)

    if(msg == ""):
     continue
    if keyboard.is_pressed("esc"):
        break
    

    #messenger api ctrls
    client.send(Message(text=msg), thread_id=1000831126693209, thread_type=ThreadType.GROUP)

    i = i+1

    print(i)

    time.sleep(2)


client.logout()