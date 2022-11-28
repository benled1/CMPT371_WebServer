from socket import *

class ProxyServer:

    def __init__(self, port, server_port, server_ip,):
        self.port = port
        self.server_ip = server_ip
        self.server_port = server_port

    def init_socket(self):
        # Create server socket
        self.socket = socket(AF_INET, SOCK_STREAM)
        #serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(('', self.port))
        self.socket.listen(1)
        pass

    def __request_server(self, request_content):
        # Create client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.server_ip, self.server_port))
        # Send the client request
        request = request_content
        clientSocket.send(request.encode())

        # Get HTTP response
        response = clientSocket.recv(1024)
        print("From Server:", response.decode())\

        # Close socket
        clientSocket.close()
        return response

    def run(self):
        print('Listening on port %s ...' % self.port)
        prev_content = ''
        while True:
            # Wait for client connections
            connectionSocket, client_addr = self.socket.accept()
        
            # Get the client request
            request = connectionSocket.recv(1024).decode()
            response = self.__request_server(request_content=request)

            # Send HTTP response
            connectionSocket.sendall(response)
            # Close socket
            connectionSocket.close()
        pass