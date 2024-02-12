import asyncio
import os
import sys



if not os.getenv('DEVICE_ID') and \
        not os.getenv('ACCOUNT_ID') and \
        not os.getenv('SECRET'):
    print("Please paste your device auths into the \".env\" file.\n")
    sys.exit()

os.system('python3 -m pip install --upgrade SEKKAYBOT ')
os.system('clear')

import SEKKAYBOT

client = SEKKAYBOT.SekkayBot(
    device_id=os.getenv('DEVICE_ID'),
    account_id=os.getenv('ACCOUNT_ID'),
    secret=os.getenv('SECRET')
)
try:
  client.run()
except Exception as e:
  print(e)
  print("Can't login because your device auths is probably wrong.")
  print("are you sure you have put your IDs in secrets env or in .device  file ?")

