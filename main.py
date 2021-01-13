import asyncio
import os
import sys
import platform
import time
import json
import datetime
import connect

time.sleep(4)

name = input("Enter your name: ")


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
    f.write(f'`{name}`: ' + message + '\n')
    f.close()

  if message == 'clear':
    clearContents()