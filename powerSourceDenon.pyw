import os
import socket
import time
import ipaddress
from dotenv import load_dotenv

load_dotenv()
IP_ADDRESS = os.getenv('DENON_IP')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, 23))

s.send(b"ZM?")
powerstate = s.recv(135)
s.send(b"SI?")
source = s.recv(135)

if powerstate == b"ZMOFF\r":
    s.send(b"ZMON")
    time.sleep(1)
    s.send(b"SIMPLAY")
    time.sleep(1)
    s.send(b"MV25")
else:
    if source == b"SITV\r":
        s.send(b"SIMPLAY")
        time.sleep(2)
        s.send(b"MV25")
    else:
        s.send(b"SITV")
        time.sleep(2)
        s.send(b"MV38")
s.close