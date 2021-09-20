# Create server socket to wait for a connection from client

import socket
sock = socket.socket()

# bind socket to accept connections from all IP addrs on port 4444
# allows one connection to socket
sock.bind(("0.0.0.0", 4444))
sock.listen(1)

# saves connection object and addr to var
conn, addr = sock.accept()
# sends welcome message to connected client, encode
conn.send("Welcome to the server".encode())
# accepts message from client, print, close
print(conn.recv(2048).decode())
sock.close()

