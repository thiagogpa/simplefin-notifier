import requests
from utils.init_logger import app_logger

class NtfyService:
    def __init__(self, url, token, priority):
        self.url = url
        self.token = token
        self.priority = priority if priority else 3
    def notify(self, title, message, priority):
        headers = { "Title": title, "Priority": str(self.priority) }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        app_logger.debug(f"Sending notification to {self.url}")
        requests.post(self.url, data=message, headers=headers)
