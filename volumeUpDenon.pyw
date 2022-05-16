import os
import socket
import time
from dotenv import load_dotenv

load_dotenv()
IP_ADDRESS = os.getenv('DENON_IP')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, 23))

for i in range(2):
    s.send(b"MVUP")
    time.sleep(0.01)

s.close