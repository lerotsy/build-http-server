# HTTP Server challenge from CodeCrafters
This is a starting point for Python solutions to the
["Build Your Own HTTP server" Challenge](https://app.codecrafters.io/courses/http-server/overview).

This is my implementation of a basic HTTP server in Python, created as part of a coding challenge by CodeCrafters. The project aims to demonstrate a fundamental understanding of HTTP protocol and server-side programming in Python. While it is not a comprehensive, full-fledged HTTP server, this project successfully satisfies the specific requirements of the CodeCrafters challenge.

## Features 
- **Handling HTTP Requests**: The server is programmed to respond with a 200 OK status for valid HTTP requests and a 404 Not Found status for invalid ones
- **Header Parsing**: 
- **Handling concurrent client connections**: supports multiple clients sending requests simultaneously
- **File Transfer Operations**: (Not yet implemented) should support `GET` a file and `POST` a file


## Potential improvements
- **Request Body Parsing**: Enhance the server's ability to parse and process the body of incoming requests, especially for different content types (like application/json)
- **MIME Type Handling**: Automatically determine and set the correct Content-Type header in responses based on the MIME type of the file or data being served

## Launching the project

To get the HTTP server up and running, as well as to test its functionality, follow these steps:

### Launching the server
- Open a terminal window and navigate to the project's root directory.
- Run the server script by executing:
`./your_server.sh`

### Launching the client
- In a separate terminal window, navigate to the client/ folder within the project repository. This directory contains a Python script designed to perform tests based on the different steps outlined in the CodeCrafters coding challenge.
- run the script 
`python http_client.py`

