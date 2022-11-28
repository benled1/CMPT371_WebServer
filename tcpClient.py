from socket import *
# Define socket host and port
SERVER_NAME = "192.168.1.215"
SERVER_PORT = 12001

# Create client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))

# Send the client request
request = "GET / HTTP/1.1\r\n/test.html\r\n"
clientSocket.send(request.encode())

# Get HTTP response
response = clientSocket.recv(1024)
print("From Server:", response.decode())\

# Close socket
clientSocket.close()

# http://192.168.1.215:12000/test.html
