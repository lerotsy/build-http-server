# Uncomment this to pass the first stage
import socket
import threading
from .request_handler import HttpRequestHandler

def handle_client_connection(client_socket):
    try:
        data = client_socket.recv(1024)
        handler = HttpRequestHandler(data)
        client_socket.send(handler.process_request().encode())
    except Exception as e:
        print("Error handling request:", str(e))
    finally:
        client_socket.close()

def main():
    print("Server is starting...")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
