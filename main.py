import asyncio
import os
import sys
import platform
import time
import json
import datetime
import connect

time.sleep(4)

options = ["Female", "Male", "female", "male"]

name = input("Enter your name: ")
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
    f.write(f'`{name}` ({gender}): ' + message + '\n')
    f.close()

  if message == 'clear':
    clearContents()