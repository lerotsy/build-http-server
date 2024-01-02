from dataclasses import dataclass

EOL = "\r\n"  # End of line
EOR = "\r\n"  # End of Response


@dataclass
class HttpResponse:
    status_code: int = 200
    content_type: str = None
    content: str = None
    user_agent: str = None

    def response_description(self) -> str:
        descriptions = {
            200: 'OK',
            404: 'NOT FOUND',
        }
        return descriptions.get(self.status_code, "OTHER")

    def to_string(self) -> str:
        response_parts = [
            (f"HTTP/1.1 {self.status_code} {self.response_description()}"
             f"{EOL}")
        ]

        if self.content_type:
            response_parts.append(f"Content-Type: {self.content_type}{EOL}")

        content_length = len(self.content) if self.content else 0
        response_parts.append(f"Content-Length: {content_length}{EOL}")
        response_parts.append(f"{EOL}")

        if self.content:
            response_parts.append(self.content)

        response_parts.append(EOR)
        return ''.join(response_parts)
