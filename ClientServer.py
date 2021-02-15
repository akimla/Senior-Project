import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('localhost', 10000)
sock.bind(server_address)
print ('starting up on %s port %s' % sock.getsockname())
sock.listen(1)

while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ('client connected:', client_address)
        while True:
            data = connection.recv(1024)
            print ('received "%s"' % data.decode())
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()