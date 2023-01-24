import socket
import sys

client_name = "Test Client"
server_port = 6000

# get the integer value from the command line
client_number = int(sys.argv[1])
if client_number > 100 or client_number < 1:
    print("Invalid client number. Terminating client.")
    sys.exit()

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect(("", server_port))

# send the client's name and number to the server
client_data = client_name + " " + str(client_number)
client_socket.send(client_data.encode())

# receive data from the server
server_data = client_socket.recv(1024).decode()
server_name, server_number = server_data.split()
server_number = int(server_number)
print("Received data from server: ", server_data)

# print the client's name and the server's name