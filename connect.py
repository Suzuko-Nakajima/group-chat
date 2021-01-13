import asyncio
import os
import sys
import platform
import json
import time
import datetime

class Connect:
  def __init__(self, main):
    self.main = main

  print('-!- ==================== -!-')
  print('- + - Program initialized - + -')
  print('-!- ==================== -!-\n\n')

def setup(main):
  main.add_cog(Connect(main()))