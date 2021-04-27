# Austin Kimla

import socket
import select
import sys
import struct
from datetime import datetime
from uuid import getnode as get_mac
from random import randint
from _thread import * 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

#Prepare a server socket
Buffer_Size = 4096
#serversIP = input("Please type in your servers IP: ")
#TCP_PORT = int(input("Please type in your servers port number: "))
server.connect(('10.40.0.115', 1337))
  
while True:  
  
    # maintains a list of possible input streams  
    sockets_list = [sys.stdin, server]  

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])  

    for socks in read_sockets:  
        if socks == server:  
            message = socks.recv(Buffer_Size).decode()
            print (message)  
        else:  
            message = sys.stdin.readline()
            server.send(bytes(message, 'utf-8'))
            sys.stdout.write("<You>")  
            sys.stdout.write(message)  
            sys.stdout.flush()  
server.close()  
