import socket
import os

HOST, PORT = '', 6789

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f'Serving HTTP on port {PORT} ...')

        while True:
            client_connection, client_address = server_socket.accept()
            request = client_connection.recv(1024).decode()
            print(f'Request: {request}')

            request_lines = request.split('\n')
            request_line = request_lines[0]
            filename = request_line.split()[1]
            filename = filename.split('/')[-1]
            print(f'Filename: {filename}')

            if not os.path.exists(filename):
                response = 'HTTP/1.1 404 Not Found\n\n'
                response += '<html><head></head><body><h1>404 Not Found</h1></body></html>'
            else:
                with open(filename, 'r') as file:
                    response = 'HTTP/1.1 200 OK\n\n'
                    response += file.read()

            client_connection.sendall(response.encode())
            client_connection.close()

if __name__ == '__main__':
    start_server()