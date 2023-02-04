import socket
import sys
import pickle
client_name = "Client of Abhir Karande"
server_port = 6000

client_number = int(sys.argv[1])
if client_number > 100 or client_number < 1:
    print("Invalid client number. Terminating client.")
    sys.exit()

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(("127.0.0.1", server_port))

client_data = pickle.dumps([client_name, client_number])
client_sock.send(client_data)

server_name, server_number = pickle.loads(client_sock.recv(1024))
server_number = int(server_number)
print("Sum of values ", client_number + server_number)

client_sock.close()