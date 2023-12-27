# Uncomment this to pass the first stage
import socket
from .request_handler import HttpRequestHandler


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, client_address = server_socket.accept() # wait for client

    
    data = client_socket.recv(1024) 


    try:
        handler = HttpRequestHandler(data)
        client_socket.send(handler.process_request().encode())  # Send the HTTP response
        # print("Sent response: HTTP/1.1 200 OK")
    except Exception as e:
        print("Error sending response:", str(e))
    finally:
        client_socket.close()  # Close the client socket


if __name__ == "__main__":
    main()
