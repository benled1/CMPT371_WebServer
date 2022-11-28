from classes.tcpProxyClass import ProxyServer

proxy_instance = ProxyServer(12001, "192.168.1.215")
proxy_instance.init_socket()
proxy_instance.run()