# Define a socket in a server using Python, wait for connection

import socket

my_sock = socket.socket()

# bind socket to accept connection from all IP addresses, port 4444
my_sock.bind(("0.0.0.0", 4444))
# allows one connection
my_sock.listen(1)
# allows connection to socket, saves connection object/addr to var, close
conn, addr = my_sock.accept()
my_sock.close()
