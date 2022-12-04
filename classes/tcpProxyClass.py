from socket import *
from datetime import datetime
import os

class ProxyServer:

    def __init__(self, port, server_port, server_ip,):
        self.port = port
        self.server_ip = server_ip
        self.server_port = server_port
        self.cache = {}
        for file in os.listdir('classes/proxycache'):
            self.cache[file] = datetime.now()

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

    def __cache_new_file(self, response, filename):
        response_lines = response.split('\n')
        html_text = '\n'.join(response_lines[1:])
        with open(f'classes/proxycache/{filename}', 'w') as f:
            f.write(html_text)
        self.cache[filename] = datetime.now()

    def __check_response_status(self, response):
        status_code = response.split(' ')[1]
        return status_code

    def __create_response_from_cache(self):
        with open('classes/proxycache/test.html', 'r') as f:
            lines = f.readlines()
            html_text = ''.join(lines)
            header_text = 'HTTP/1.1 200 OK\n'
            response_text = header_text + html_text
        return response_text

    def __request_server_cond(self, request_content, filename):
        # Create client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.server_ip, self.server_port))
        # Send the client request
        request = request_content + f"If-modified-since {self.cache[filename]}"
        print(request)
        clientSocket.send(request.encode())

        # Get HTTP response
        response = clientSocket.recv(1024)

        # Close socket
        clientSocket.close()
        return response

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
            filename = request.split('\n')[1][1:-1]
            is_cached = self.__check_cache(filename=filename)
            if not is_cached:
                response = self.__request_server(request_content=request)
                decoded_response = response.decode()
                self.__cache_new_file(response=decoded_response, filename=filename)
                print(self.cache)
                

            else:
                response = self.__request_server_cond(request_content=request, filename=filename)
                decoded_response = response.decode()
                status = self.__check_response_status(response=decoded_response)
                print(status)
                if status == '304':
                    #craft some response from the cached item
                    response_text = self.__create_response_from_cache()
                    print(response_text)
                    response = response_text.encode()
                else:
                    self.__cache_new_file(response=decoded_response, filename='test.html')
                    

            # Send HTTP response
            connectionSocket.sendall(response)
            # Close socket
            connectionSocket.close()