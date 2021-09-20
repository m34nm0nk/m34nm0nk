# Creates client to connect to server, perform authentication process

import socket
s = socket.socket()
s.connect(("127.0.0.1", 1234))
# prints first welcome message from server
print(s.recv(2048).decode())
# get input for username, sent to server
s.send(input("").encode())
# prints second message from server, requests password, send to server
# print final message regarding authentication success/failure
print(s.recv(2048).decode())
s.send(input("").encode())
print(s.recv(2048).decode())
s.close()
