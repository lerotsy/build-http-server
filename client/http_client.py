import socket
import threading


def log_info(custom_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(custom_message)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def create_http_request(method, url, host, user_agent=None, body=None):
    request_line = f"{method} {url} HTTP/1.1\r\n"
    headers = f"Host: {host}\r\n"
    if user_agent:
        headers += f"User-Agent: {user_agent}\r\n"

    if body:
        headers += f"Content-Length: {len(body)}\r\n"

    headers += "\r\n"
    return request_line + headers + (body if body else "")


def send_request(method, url, user_agent=None, body=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 4221))
    request = create_http_request(method, url, 'localhost', user_agent, body)
    client_socket.send(request.encode())

    response = client_socket.recv(4096)
    print(f"Response from server:\n{response.decode()}\n")
    client_socket.close()

    # Extract the status code from the response
    status_line = response.decode().split('\r\n')[0]
    status_code = int(status_line.split(' ')[1])
    return status_code, response


@log_info("Sending GET /echo/xyz ")
def test_get_valid_url():
    status_code, response = send_request("GET", "/echo/xyz")
    assert status_code == 200, f"Expected status code 200, got {status_code}"


@log_info("Sending request for / ")
def test_valid_with_user_agent():
    status_code, response = send_request(
        "GET", "/user-agent", user_agent='curl/7.64.1')
    assert status_code == 200, f"Expected status code 200, got {status_code}"


@log_info("Sending GET invalid url")
def test_get_invalid_url():
    status_code, response = send_request("GET", "/invalid-url")
    assert status_code == 404, f"Expected status code 404, got {status_code}"


def test_post_file():
    file_content = "This is a test file."
    send_request("POST", "/upload", file_content)


@log_info("sending 5 valid url concurrently")
def test_concurrent_requests():
    threads = []
    for i in range(5):  # Example: 5 concurrent requests
        thread = threading.Thread(target=test_get_valid_url)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    test_get_valid_url()
    test_get_invalid_url()
    test_valid_with_user_agent()
    test_concurrent_requests()
    # test_post_file()
