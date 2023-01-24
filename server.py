import socket
import random

server_name = "Server of John Q. Smith"
server_port = 6000 # choose a port number greater than 1023

# create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the server address and port
server_socket.bind(("", server_port))

# listen for incoming connections
server_socket.listen(1)

while True:
    # accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print("Connected to ", client_address)
    
    # receive data from the client
    client_data = client_socket.recv(1024).decode()
    client_name, client_number = client_data.split()
    client_number = int(client_number)
    print("Received data from client: ", client_data)
    
    if client_number > 100 or client_number < 1:
        print("Invalid client number. Terminating server.")
        server_socket.close()
        break
        
    # pick a random number between 1 and 100
    server_number = random.randint(1, 100)
    print("Server number: ", server_number)
    
    # print the client's name and the server's name
    print("Client name: ", client_name)
    print("Server name: ", server_name)
    
    # compute the sum of the two numbers
    sum_of_numbers = client_number + server_number
    print("Sum of values: ", sum_of_numbers)
    
    # send the server's name and number back to the client
    server_data = server_name + " " + str(server_number)
    client_socket.send(server_data.encode())
    
    # close the client socket
    client_socket.close()