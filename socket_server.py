# Source modified from: realpython.com/python_sockets
# Author: miti@phas.ubc.ca
# Created on: 2024-01-10

import socket

HOST = "127.0.0.1" # address of server (local host)
PORT = 65432 # ports higher than 1023 are not usally reserved

# We will create a server socket and listen on it.

# @brief SOCK_STREAM: specifies socket uses TCP
# @brief SOCK_DGRAM: specifies socket uses UDP
# @brief AF_INET: specifies socket uses IPv4

# Using "with" make it so the server_socekt.close() is called automatically 
# when program ends outside the scope of the with statement.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # These next 3 lines calls set-up a "listening" socket
    server_socket.bind((HOST, PORT)) # bind the socket to an IP and port number
    server_socket.listen() # make the socket a listening socket

    # @param client_socket is used to communicate with the client
    # @param addr is the address of the client
    # @brief accept() blocks execution and waits for an incoming connection
    client_socket, client_addr = server_socket.accept() 

    # Once client connects we will stay in this while loop and process data:
    with client_socket:
        print(f"Connected by {client_addr}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)

