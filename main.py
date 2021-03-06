import asyncio
import os
import sys
import platform
import time
import json
import datetime
import connect

confirmationChoices = ["Yes", "No", "yes", "no"]

def shutdown():
    global confirmation
    confirmation = input("Are you sure you want to shutdown the program?\n")
    if confirmation not in confirmationChoices:
        print('Error: That isn\'t a valid option.')
    elif confirmation == 'Yes' or confirmation == 'yes':
        exit()
    elif confirmation == 'No' or confirmation == 'no':
        print('The program is still running.\nReason: Shutdown declined.')

prefix = './'

def chooseName():
    global name
    name = input("Enter your name: ")

def chooseGender():
    global gender
    gender = input("Gender (Female | Male): ")

def helpList():
    print("\nAll commands begin with a './' prefix.\n\n1. clear\n2. gender\n3. shutdown\n4. updatename\n5. urm\n")

def updateREADME():
  if os.path.exists("README.md"):
    global rmMessage
    rmMessage = input("Update README: ")

    with open("README.md", "a") as f:
      f.write(rmMessage + '\n\n')
  else:
    with open("README.md", "x") as f:
      f.close()
      print('The README file has been created.\nExecute this command again to use the file.')


time.sleep(4)

options = ["Female", "Male", "female", "male"]
chooseName()
age = int(input("Enter your age: "))

chooseGender()
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

        if message == prefix + 'gender':
            chooseGender()

        if message == prefix + 'urm':
          updateREADME()

        if message == prefix + 'shutdown':
            shutdown()