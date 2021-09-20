# Creates client socket, connect to server, receive message, reply

import socket
sock = socket.socket()
sock.connect(("127.0.0.1", 4444))
# receive message from server, print
print(sock.recv(2048).decode())
# return message to server, close
sock.send("Thanks!".encode())
sock.close()
