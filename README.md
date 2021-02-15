# Senior-Project

# ClientServer.py is meant to look for clients that are awaiting to find a connection and provide them with an IP like a DHCP server.
# Client.py is meant to accept that incoming connection and link up with the server via a handshake and provide a message saying connected and report details such as IP, hostname, etc.

# It now connects to different clients on different ports. Sends a message to notify confirmation of handshake.
# Currently, it is missing a decode line for each file to get rid of the b' for a bytes object. Once added, project should be officially finished.
# Across computer access should require changing IP instead of using localhost.
