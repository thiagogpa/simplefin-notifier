import requests

class TelegramService:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def notify(self, title, message, priority):
        payload = {
            "chat_id": self.chat_id,
            "text": f"*{title}*\n{message}",
            "parse_mode": "Markdown"
        }
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        requests.post(url, data=payload)
