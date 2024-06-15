import requests

class DiscordService:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def notify(self, title, message, priority):
        payload = {
            "content": f"**{title}**\n{message}"
        }
        requests.post(self.webhook_url, json=payload)
