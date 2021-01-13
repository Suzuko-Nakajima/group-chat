import asyncio
import os
import sys
import platform
import time
import json
import datetime
import connect

def shutdown():
    print('The program has shutdown.')
    exit()

prefix = './'

def chooseName():
    global name
    name = input("Enter your name: ")

def helpList():
    print("All commands begin with a './' prefix.\n\n1. clear\n2. updatename\n3. shutdown")


time.sleep(4)

options = ["Female", "Male", "female", "male"]
chooseName()
age = int(input("Enter your age: "))

gender = input("Gender (Female | Male): ")
if gender not in options:
    print(f'Error: \"{gender}\" is not a valid gender.')
    exit()

if age < 13:
    print('Due to your age, you are not allowed to talk here.')
    exit()


if os.path.exists("groupChat.md"):
  pass
else:
  with open("groupChat.md", "x") as f:
    f.write("## Markdown File - Group Chat\n- You can use this file to receive your output messages.\n\n")
    f.close()

while True:
    message = input("Enter a message: ")

    def clearContents():
        with open("groupChat.md", "w+") as f:
            f.write("## Markdown File - Group Chat\n- You can use this file to receive your output messages.\n\n")
            f.close()

  
    with open("groupChat.md", "a") as f:
        if prefix not in message:
            f.write(f'`{name}` ({gender}): ' + message + '\n')
            f.close()

        if message == prefix + 'help':
            helpList()

        if message == prefix + 'clear':
            clearContents()

        if message == prefix + 'updatename':
            chooseName()


        if message == prefix + 'shutdown':
            shutdown()