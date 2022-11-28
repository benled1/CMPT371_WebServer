from socket import *

class ProxyServer:

    def __init__(self, port, server_ip):
        self.port = port
        self.server_ip = server_ip

    def init_socket(self):
         # Create server socket
        self.socket = socket(AF_INET, SOCK_STREAM)
        #serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(('', self.port))
        self.socket.listen(1)
        pass

    def __request_server():
        pass

    def run(self):
        print('Listening on port %s ...' % self.port)
        prev_content = ''
        while True:
            # Wait for client connections
            connectionSocket, client_addr = self.socket.accept()
        
            # Get the client request
            request = connectionSocket.recv(1024).decode()
            print(request)

            # Parse HTTP headers
            headers = request.split('\n')
            filename = headers[1].split()[0]
            print(filename)
            if headers[0].split()[0] != 'GET' or headers[0].split()[2] != 'HTTP/1.1':
                response = 'HTTP/1.1 400 BAD REQUEST\n\nBad Request'

            elif headers[0].split()[1] == '/' and filename != '/test.html':
                response = 'HTTP/1.1 404 NOT FOUND\n\n%s Not Found' % filename

            elif headers[0].split()[1] == '/' and filename == '/test.html':
                webpage = open('.' + filename)
                content = webpage.read()
                if content != prev_content:
                    prev_content = content
                    webpage.close()
                    response = 'HTTP/1.1 200 OK\n\n' + content 
                else:
                    webpage.close()
                    response = 'HTTP/1.1 304 NOT MODIFIED\n\nNot Modified'

            # Send HTTP response
            connectionSocket.sendall(response.encode())
            # Close socket
            connectionSocket.close()
        pass