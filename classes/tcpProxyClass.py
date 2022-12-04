from socket import *
from datetime import datetime
import os

class ProxyServer:

    def __init__(self, port, server_port, server_ip,):
        self.port = port
        self.server_ip = server_ip
        self.server_port = server_port
        self.cache = {}

    def init_socket(self):
        # Create server socket
        self.socket = socket(AF_INET, SOCK_STREAM)
        #serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(('', self.port))
        self.socket.listen(1)
        pass

    def __check_cache(self, filename):
        if filename in os.listdir('classes/proxycache'):
            return True
        else:
            return False

    def __request_server_cond(self, request_content, filename):
        # Create client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.server_ip, self.server_port))
        # Send the client request
        request = request_content + f"If-modified-since {self.cache[filename]}"
        clientSocket.send(request.encode())

        # Get HTTP response
        response = clientSocket.recv(1024)

        # Close socket
        clientSocket.close()

    def __request_server(self, request_content):
        # Create client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.server_ip, self.server_port))
        # Send the client request
        request = request_content
        clientSocket.send(request.encode())

        # Get HTTP response
        response = clientSocket.recv(1024)

        # Close socket
        clientSocket.close()
        return response

    def run(self):
        print('Listening on port %s ...' % self.port)
        while True:
            # Wait for client connections
            connectionSocket, client_addr = self.socket.accept()
        
            # Get the client request
            request = connectionSocket.recv(1024).decode()
            filename = request.split('\n')[1][1:]
            is_cached = self.__check_cache(filename=filename)
            if not is_cached:
                response = self.__request_server(request_content=request)
                print("RESPONSE FROM THE SERVER")
                print(response)
                # when this returns from the server, it will have html text contained within it
                # take the html text, create a file with the same name and store the text in that file in the proxycache
            else:
                response = self.__request_server_cond(request_content=request, filename=filename)
                # when this returns, we will get one of two things, either we will get a 304 or a response 200 containing an html text
                # if we get a 304, then create a response containing the html file we already have cached and return it
                # if we get a 200, then just padd that along as the response

            # Send HTTP response
            connectionSocket.sendall(response)
            # Close socket
            connectionSocket.close()