from typing import Union

EOL = "\r\n"  # End of line
EOR = "\r\n"  # End of Response

HTTP_GET = "GET"
HTTP_POST = "POST"
HTTP_VERBS = (HTTP_GET, HTTP_POST)

VALID_PATHS = (
    '/'
)


class HttpRequestHandler:
    def __init__(self, request_data):
        self.request_data = request_data
        self.response = None

    def get_url(self) -> Union[str, None]:
        lines = self.request_data.split(b'\n')
        first_line = lines[0].strip()  # first line should contain the verb and URL

        parts = first_line.split(b' ')
        if len(parts) >= 2 and parts[0] in HTTP_VERBS:
            url = parts[1]
            return url if url in VALID_PATHS else None
        else:
            return None


    def process_request(self) -> str:
        url = self.get_url()
        response = self.build_response(url)
        return response

    def build_response(self, url: Union[str, None]) -> str:
        if url is None:
            return f"HTTP/1.1 404 Not Found{EOL}{EOR}"
        else:
            return f"HTTP/1.1 200 OK{EOL}{EOR}"
