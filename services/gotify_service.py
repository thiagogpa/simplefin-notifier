from gotify import Gotify

class GotifyService:
    def __init__(self, base_url, app_token):
        self.gotify = Gotify(base_url=base_url, app_token=app_token)

    def notify(self, title, message, priority):
        self.gotify.create_message(message, title=title, priority=priority)
