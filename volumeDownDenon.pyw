import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.178.38", 23))

for i in range(2):
    s.send(b"MVDOWN")
    time.sleep(0.01)

s.close