# Austin Kimla

# TODO:
# 1.) Add a timestamp and lease time (DONE)
# 2.) Make the Server run globally instead of peer to peer (DONE)
# 3.) Add a pool of addresses to offer up along with ports (DONE) -sidenote: Couldn't find an automatic way, so did it manually with each computers IP
# 4.) Assignment & Reuse IP after lease time expires (Semi-Done) -sidenote: The IP and ports are reusable after the connection has been severed
# However, did not find a way or think of a way to automatically take that IP away or close the connection after that time is expired
# 5.) Use Jinja or Quik to make a 1 page webpage to vizualize DHCP Server. (Incomplete) -sidenote: Did not get to this part of the goals, but have very visual
# idea in mind that can be drawn out to illustrate the process.

import socket
import select
import sys
import struct
import random
from datetime import datetime, timedelta
from random import randint
from _thread import *

# TCP/IP Server Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Preparing the Socket
TCP_PORT = 1337
Buffer_Size = 4096
server.bind(('0.0.0.0', TCP_PORT)) # 0.0.0.0 opens connection to all interfaces same as 255.255.255.255
server.listen(100) # Allows 100 clients to connect and get a DHCP Offer from Discovery

list_of_clients = []

# Server IPs and Ports for DHCP to give out and offer
ServerIPs = {1: "10.40.0.107", 2: "10.40.0.108", 3: "10.40.0.109", 4: "10.40.0.112", 5: "10.40.0.115", 6: "10.40.0.116", 7: "10.40.0.117"}
ServerPorts = {1: "1337", 2: "1338", 3: "1339", 4: "1340", 5: "1341", 6: "1342", 7: "1343"}

# DHCP Server has started
print("Mock DHCP Server is now running...")

def clientthread(conn, addr):
    # Start of connection info

    conn.send("Mock DHCP Info from Discover Below: \n".encode())
    conn.send("\n".encode())
    conn.send("Selected IP from Discovery: ".encode())
    conn.send(random.choice(list(ServerIPs.values())).encode())
    conn.send("Selected Port from Discovery: ".encode())
    conn.send(random.choice(list(ServerPorts.values())).encode())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    OneMinute = (datetime.now() + timedelta(minutes = 1)).strftime("%H:%M:%S")
    conn.send("Current Time: ".encode())
    conn.send(current_time.encode())
    conn.send("Lease Time: ".encode())
    conn.send(OneMinute.encode())


    # End of connection info

    while True:
            try:
                message = conn.recv(Buffer_Size).decode()
                if message:
                    print ("<" + addr[0] + "> " + message)
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send, conn)
                else:
                    remove(conn)
            except:
                continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message).encode() 
            except:  
                clients.close() 
                remove(clients)

def remove(connection):  
    if connection in list_of_clients:  
        list_of_clients.remove(connection)
        print(addr[0] + " has disconnected from the DHCP Server")

while True:  
    conn, addr = server.accept()  
    list_of_clients.append(conn)  
    print (addr[0] + " connected") 
    start_new_thread(clientthread,(conn,addr))  

def main():
    clientthread()
    broadcast()
    remove()

main()  

conn.close()  
server.close()  
