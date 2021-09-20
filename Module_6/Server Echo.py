# Creates server with login dialog, asks for client to insert
# username and password for authentication

import socket
s = socket.socket()
s.bind(("0.0.0.0", 1234))
s.listen(1)
conn, addr = s.accept()
# send welcome message to connected client, request username
conn.send("Welcome to the server!\nPlease insert username:".encode())
# accepts username sent by client, saves to var
username = conn.recv(2048).decode()
# requests password from client
conn.send("Please enter password: ".encode())
# accepts password from client
password = conn.recv(2048).decode()

# creates condition to check if username if 'John', passwd '123456'
# if so, server sends welcome message
if username == "John" and password == "123456":
    conn.send(f"Welcome {username}".encode())
else:
    conn.send("Wrong credentials".encode())

s.close()