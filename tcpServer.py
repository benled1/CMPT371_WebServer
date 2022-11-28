from classes.tcpServerClass import Server

server_instance = Server(12000)
server_instance.init_socket()
server_instance.run()
