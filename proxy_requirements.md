# Proxy Server Details

This file contains the details and specifications for implementing a proxy server between the tcpClient and the tcpServer.

## High Level Requirements:

- Keep a cache of all the previously requested items and store when they were last modified.
- Recieve all the HTTP requests from the requesting client.
- When a client request is received, do the following:
  - Check to see if the requested item is cached in the proxy
  - If the requested item is cached, perform a conditional get request to the web server
  - If the requested item is NOT cached, perform a typical get request to the web server



### TODO
- implement the code to have the proxy server populate its cache dictionary from the ./proxycache/ folder files
- implement the code to have the client make a first request to the proxy server and then the proxy server retrieves the html file and makes an initial cache.
- implement the code to have the client make another request for the same file, and the proxy server just returns that file from the cache after making a request to the server and getting a 304
- implement the code to have the client make another request for the same file, but this time the file has been modified on the server, so when the proxy server goes to check the file, it gets a file back in response, updates its own file, and then sends the updated file back to the client.


- When the server sends back a 304 we need to send back the file we have cached
- implement a cache function to make sure we save the file we have


