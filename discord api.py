import discord
import time
import requests
from getpass import getpass
import keyboard
import asyncio

#log into discord
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('stop'):
        await myfunc(open("D:/B._programeren/Pyhton/spamApps/stop.txt", "r"), message)

    elif message.content.startswith("rick"):
        a = open("D:\B._programeren\Pyhton\spamApps\wick.txt", "r")
        await myfunc(a, message)

    elif message.content.startswith("I wonder"):
        b =  open("D:/B._programeren/Pyhton/spamApps/wonder.txt", "r")
        await  myfunc(b, message)
    
    elif message.content.startswith("play a game"):
        for i in range(5):
            await message.channel.send("the game", tts = True)
            i = i + 1
            if keyboard.is_pressed("esc"):
                break
            await asyncio.sleep(2)

    elif  message.content.startswith("hey bot"):
        await message.channel.send("yes master", tts=True)
    
    elif message.content.startswith("dorime"):
        a = open("D:/B._programeren/Pyhton/spamApps/dorime.txt", "r")
        await myfunc(a, message)
    
    elif message.content.startswith("creeper"):
        a = open("D:/B._programeren/Pyhton/spamApps/revenge.txt", "r")
        await myfunc(a, message)
    
    elif message.content.startswith("welcome"):
        await message.channel.send("hello world")
    
    elif message.content.startswith("what are your intentions?"):
        await message.channel.send("nunya", tts = True)

    elif message.content.startswith("happy birthday"):
        print("recieved " + message.content)
        with open('D:/B._programeren/Pyhton/spamApps/bday.txt', 'r') as file:
            data = file.read()
            bac = data
        data = data.replace('(name)', message.content[14:])

        with open('D:/B._programeren/Pyhton/spamApps/bday.txt', 'w') as file:
            file.write(data)

        a = open('D:/B._programeren/Pyhton/spamApps/bday.txt', 'r')
        await myfunc(a, message)

        with open('D:/B._programeren/Pyhton/spamApps/bday.txt', 'w') as file:
            file.write(bac)
    elif message.content.startswith("A new challenger approaches"):
        await message.channel.send("And now, the communist manifesto", tts = True)
        a = open('D:/B._programeren/Pyhton/spamApps/God.txt', 'r')
        await myfunc(a, message)

async def myfunc(txt, mes):
    for word in txt:
        #formulate message
        msg = word
        print(msg)

        if(msg == ""):
            continue
        if keyboard.is_pressed("esc"):
            break         

        #discord api ctrls

        await mes.channel.send(msg)

        await asyncio.sleep(0.5)

client.run("Redacted")
