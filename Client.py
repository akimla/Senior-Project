import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = ('localhost', 10000)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    
    message = 'You have completed the handshake.'
    print ('sending "%s"' % message)
    sock.sendall(str.encode(message))

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print ('received "%s"' % data.decode())

finally:
    sock.close()