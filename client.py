import socket
import sys
import pickle
client_name = "Client of Abhir Karande"
server_port = 6000

# get the integer value from the command line
client_number = int(sys.argv[1])
if client_number > 100 or client_number < 1:
    print("Invalid client number. Terminating client.")
    sys.exit()

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect(("127.0.0.1", server_port))

# send the client's name and number to the server
client_data = pickle.dumps([client_name, client_number])
client_socket.send(client_data)

# receive data from the server
server_name, server_number = pickle.loads(client_socket.recv(1024))
server_number = int(server_number)
print("Sum of values ", client_number + server_number)

client_socket.close()