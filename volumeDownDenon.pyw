import os
import socket
import time
from dotenv import load_dotenv

load_dotenv()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((os.getenv('DENON_IP'), 23))

for i in range(2):
    s.send(b"MVDOWN")
    time.sleep(0.01)

s.close