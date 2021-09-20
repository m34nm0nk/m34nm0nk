# Creates a socket for the client's connection to netcat listener

import socket
import time

mysocket = socket.socket()
mysocket.connect(("10.0.0.129", 4444))

# adds a pause of 5 seconds after the connection using time module
time.sleep(5)
mysocket.close()
