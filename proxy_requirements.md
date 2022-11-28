# Proxy Server Details

This file contains the details and specifications for implementing a proxy server between the tcpClient and the tcpServer.

## High Level Requirements:

- Keep a cache of all the previously requested items and store when they were last modified.
- Recieve all the HTTP requests from the requesting client.
- When a client request is received, do the following:
  - Check to see if the requested item is cached in the proxy
  - If the requested item is cached, perform a conditional get request to the web server
  - If the requested item is NOT cached, perform a typical get request to the web server