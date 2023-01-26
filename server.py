import socket
import random
import pickle
server_name = "Server of Abhir Karande"
server_port = 6000 # choose a port number greater than 1023

# create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the server address and port
server_socket.bind(("127.0.0.1", server_port))

# listen for incoming connections
server_socket.listen(1)


while True:
    # accept a connection from a client
    client_socket, client_address = server_socket.accept()
    
    
    # receive data from the client
    client_name, client_number = pickle.loads(client_socket.recv(1024))
    print("The server of ", server_name, " is communicating with ", client_name)
    client_number = int(client_number)
    
    if client_number > 100 or client_number < 1:
        print("Invalid client number. Terminating server.")
        server_socket.close()
        break
        
    # pick a random number between 1 and 100
    server_number = random.randint(1, 100)

    server_data = pickle.dumps([server_name, server_number])    
    client_socket.send(server_data)
    client_socket.close()