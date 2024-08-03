import os
import base64
from typing import Optional
from dotenv import dotenv_values, set_key
from cryptography.fernet import Fernet
from utils.init_logger import app_logger

DEFAULT_CREDENTIALS_PATH = "./credentials"
DEFAULT_CLIENT_SECRET_FILE = "client_secret.json"
DEFAULT_FILE_LOGGING_LEVEL = "INFO"
DEFAULT_ENCRYPTION_KEY_LENGTH = 32

def generate_new_key():
    key = Fernet.generate_key().decode()  # Generate the key and decode to string
    return key

def validate_encryption_key(key: str) -> bool:
    try:
        decoded_key = base64.urlsafe_b64decode(key.encode())
        if len(decoded_key) != 32:
            app_logger.critical(f"ENCRYPTION_KEY must be 32 url-safe base64-encoded bytes.")
            exit()
        
        fernet = Fernet(key.encode())
        test_token = fernet.encrypt(b"test")
        fernet.decrypt(test_token)
        
        return True
    except ValueError as e:
        app_logger.critical(f"Encryption key is invalid \n{ValueError}")
        return False

def load_environment_variables() -> None:
    # Load environment variables from .env file
    env_vars = dotenv_values(".env")

    # Access the environment variables
    try:
        os.environ.setdefault("CREDENTIALS_PATH", env_vars.get("CREDENTIALS_PATH", DEFAULT_CREDENTIALS_PATH))
        os.environ.setdefault("FILE_LOGGING_LEVEL", env_vars.get("FILE_LOGGING_LEVEL", DEFAULT_FILE_LOGGING_LEVEL))
        os.environ.setdefault("SIMPLEFIN_BRIDGE_TOKEN", env_vars.get("SIMPLEFIN_BRIDGE_TOKEN", ""))
        os.environ.setdefault("GOTIFY_BASE_URL", env_vars.get("GOTIFY_BASE_URL", ""))
        os.environ.setdefault("GOTIFY_APP_TOKEN", env_vars.get("GOTIFY_APP_TOKEN", ""))
        os.environ.setdefault("DISCORD_WEBHOOK_URL", env_vars.get("DISCORD_WEBHOOK_URL", ""))
        os.environ.setdefault("TELEGRAM_BOT_TOKEN", env_vars.get("TELEGRAM_BOT_TOKEN", ""))
        os.environ.setdefault("TELEGRAM_CHAT_ID", env_vars.get("TELEGRAM_CHAT_ID", ""))
        os.environ.setdefault("ENCRYPTION_KEY", env_vars.get("ENCRYPTION_KEY", ""))
        os.environ.setdefault("NTFY_TOKEN", env_vars.get("NTFY_TOKEN", ""))
        os.environ.setdefault("NTFY_URL", env_vars.get("NTFY_URL", ""))
        os.environ.setdefault("NTFY_PRIORITY", env_vars.get("NTFY_PRIORITY", "3"))
    except KeyError as e:
        app_logger.error(f"Environment variable not informed: {e}")

    # If ENCRYPTION_KEY is not set, generate a new one
    if not os.environ.get("ENCRYPTION_KEY"):
        new_encryption_key = generate_new_key()
        os.environ["ENCRYPTION_KEY"] = new_encryption_key
        app_logger.warning(f"New encryption key generated: {new_encryption_key}")
        set_key(".env", "ENCRYPTION_KEY", new_encryption_key)
        app_logger.warning("New encryption key appended to the .env file")
    else :
        validate_encryption_key(os.environ["ENCRYPTION_KEY"])

    # Override with environment variables from Docker Compose (if present)
    os.environ["CREDENTIALS_PATH"] = os.environ.get("CREDENTIALS_PATH", os.environ["CREDENTIALS_PATH"])
    os.environ["FILE_LOGGING_LEVEL"] = os.environ.get("FILE_LOGGING_LEVEL", os.environ["FILE_LOGGING_LEVEL"])
    os.environ["SIMPLEFIN_BRIDGE_TOKEN"] = os.environ.get("SIMPLEFIN_BRIDGE_TOKEN", os.environ["SIMPLEFIN_BRIDGE_TOKEN"])
    os.environ["GOTIFY_BASE_URL"] = os.environ.get("GOTIFY_BASE_URL", os.environ["GOTIFY_BASE_URL"])
    os.environ["GOTIFY_APP_TOKEN"] = os.environ.get("GOTIFY_APP_TOKEN", os.environ["GOTIFY_APP_TOKEN"])
    os.environ["DISCORD_WEBHOOK_URL"] = os.environ.get("DISCORD_WEBHOOK_URL", os.environ["DISCORD_WEBHOOK_URL"])
    os.environ["TELEGRAM_BOT_TOKEN"] = os.environ.get("TELEGRAM_BOT_TOKEN", os.environ["TELEGRAM_BOT_TOKEN"])
    os.environ["TELEGRAM_CHAT_ID"] = os.environ.get("TELEGRAM_CHAT_ID", os.environ["TELEGRAM_CHAT_ID"])
    os.environ["ENCRYPTION_KEY"] = os.environ.get("ENCRYPTION_KEY", os.environ["ENCRYPTION_KEY"])
    os.environ["NTFY_TOKEN"] = os.environ.get("NTFY_TOKEN", os.environ["NTFY_TOKEN"])
    os.environ["NTFY_URL"] = os.environ.get("NTFY_URL", os.environ["NTFY_URL"])
    os.environ["NTFY_PRIORITY"] = os.environ.get("NTFY_PRIORITY", os.environ["NTFY_PRIORITY"])

# Load environment variables
load_environment_variables()

# Access the environment variables
FILE_LOGGING_LEVEL: str = os.environ["FILE_LOGGING_LEVEL"]
CREDENTIALS_PATH: str = os.environ["CREDENTIALS_PATH"]
SIMPLEFIN_BRIDGE_TOKEN: str = os.environ["SIMPLEFIN_BRIDGE_TOKEN"]
GOTIFY_BASE_URL: Optional[str] = os.environ.get("GOTIFY_BASE_URL")
GOTIFY_APP_TOKEN: Optional[str] = os.environ.get("GOTIFY_APP_TOKEN")
DISCORD_WEBHOOK_URL: Optional[str] = os.environ.get("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN: Optional[str] = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID: Optional[str] = os.environ.get("TELEGRAM_CHAT_ID")
ENCRYPTION_KEY: str = os.environ["ENCRYPTION_KEY"]
NTFY_TOKEN: Optional[str] = os.environ.get("NTFY_TOKEN")
NTFY_URL: Optional[str] = os.environ.get("NTFY_URL")
NTFY_PRIORITY: Optional[str] = os.environ["NTFY_PRIORITY"]