from config.env_config import (
    GOTIFY_APP_TOKEN,
    GOTIFY_BASE_URL,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    DISCORD_WEBHOOK_URL
)

from services.notification_service import NotificationService
from services.gotify_service import GotifyService
from services.discord_service import DiscordService
from services.telegram_service import TelegramService



class NotificationSetup:
    def __init__(self):
        self.notification_service = NotificationService()

    def setup_gotify(self):
        gotify_base_url = GOTIFY_BASE_URL
        gotify_app_token = GOTIFY_APP_TOKEN
        if gotify_base_url and gotify_app_token:
            gotify_service = GotifyService(gotify_base_url, gotify_app_token)
            self.notification_service.add_service(gotify_service)

    def setup_discord(self):
        discord_webhook_url = DISCORD_WEBHOOK_URL
        if discord_webhook_url:
            discord_service = DiscordService(discord_webhook_url)
            self.notification_service.add_service(discord_service)

    def setup_telegram(self):
        telegram_bot_token = TELEGRAM_BOT_TOKEN
        telegram_chat_id = TELEGRAM_CHAT_ID
        if telegram_bot_token and telegram_chat_id:
            telegram_service = TelegramService(telegram_bot_token, telegram_chat_id)
            self.notification_service.add_service(telegram_service)

    def setup_notifications(self):
        self.setup_gotify()
        self.setup_discord()
        self.setup_telegram()
        return self.notification_service
