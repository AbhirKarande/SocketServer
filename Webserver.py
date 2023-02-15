from socket import *

server_port = 6789
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

while True:
    connection_socket, address = server_socket.accept()
    
    with connection_socket:
        try:
            request = connection_socket.recv(1024).decode().splitlines()
            filename = request[0].split()[1][1:]
            with open(filename, 'r') as file:
                contents = file.read()
                response = f"HTTP/1.1 200 OK\r\n\r\n{contents}"
                connection_socket.sendall(response.encode())
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\n\r\n" \
                       "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
            connection_socket.sendall(response.encode())

server_socket.close()