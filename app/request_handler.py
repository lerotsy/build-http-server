from typing import Union
from .http_response import HttpResponse
import re

EOL = "\r\n"  # End of line
EOR = "\r\n"  # End of Response

HTTP_GET = "GET"
HTTP_POST = "POST"
HTTP_VERBS = (HTTP_GET, HTTP_POST)

VALID_PATHS = (
    '/index'
)


class HttpRequestHandler:
    def __init__(self, request_data):
        self.request_data = request_data
        self.response = None

    def get_url(self) -> Union[str, None]:
        lines = self.request_data.decode('utf-8').split('\n')
        first_line = lines[0].strip()  # first line should contain the verb and URL

        parts = first_line.split(' ')
        if len(parts) >= 2 and parts[0] in HTTP_VERBS:
            url = parts[1]
            return url if is_valid_path(url) else None
        else:
            return None


    def process_request(self) -> str:
        url = self.get_url()
        if url is None:
            response = HttpResponse(status_code=404)
        else:
            url_parts = url.split('/echo/')
            content = url_parts[1] if len(url_parts) > 1 else None
            response = HttpResponse(content_type='text/plain', content=content)
        return response.to_string()

def is_valid_path(url: str):
    if url in VALID_PATHS:
        return True
    
    if re.match(r'/echo/[^/]+$', url):
        return True
    
    return False