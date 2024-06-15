import os
import requests
import json
import base64
from cryptography.fernet import Fernet, InvalidToken
from config.env_config import CREDENTIALS_PATH, SIMPLEFIN_BRIDGE_TOKEN, ENCRYPTION_KEY
from utils.init_logger import app_logger

class SimpleFINCredentialSetup:
    def __init__(self):
        self.simplefin_auth_file = os.path.join(CREDENTIALS_PATH, "simplefin_auth.json")
        self.fernet = Fernet(ENCRYPTION_KEY.encode())

    def setup_credentials(self):
        if not os.path.exists(self.simplefin_auth_file):
            self.create_credentials_from_token()
        else:
            self.validate_credentials()

    def create_credentials_from_token(self):
        app_logger.info("No prior SimpleFIN credentials found, creating from token...")
        sf_token = SIMPLEFIN_BRIDGE_TOKEN
        res = requests.post(base64.b64decode(sf_token))

        if res.status_code != 200:
            app_logger.error(
                "SimpleFIN setup token invalid. Has it been used already? If so, delete the token from your account, generate a new one, and update .env."
            )
            exit()
        else:
            app_logger.info("SimpleFIN setup token valid. Saving access credentials.")

        self.save_credentials(res.text)

    def save_credentials(self, access_url):
        scheme, rest = access_url.split("//", 1)
        auth, rest = rest.split("@", 1)
        url = scheme + "//" + rest + "/accounts"
        username, password = auth.split(":", 1)

        simplefin_data = {"url": url, "username": username, "password": password}

        encrypted_data = self.fernet.encrypt(json.dumps(simplefin_data).encode())

        with open(self.simplefin_auth_file, "wb") as f:
            f.write(encrypted_data)
            app_logger.info("SimpleFIN credentials saved (encrypted).")

    def validate_credentials(self):
        app_logger.info("Validating SimpleFIN credentials...")
        with open(self.simplefin_auth_file, "rb") as f:
            encrypted_data = f.read()

        try:
            decrypted_data = self.fernet.decrypt(encrypted_data).decode()
        except InvalidToken:
            app_logger.critical("Encryption key does not match, unable to decrypt credential file")
            exit()
            
        sf_auth = json.loads(decrypted_data)

        res = requests.get(
            sf_auth["url"], auth=(sf_auth["username"], sf_auth["password"])
        )
        if res.status_code != 200:
            app_logger.info(
                "SimpleFIN credentials invalid. Please check your credentials and try again. Specific setup information is available in the README."
            )
            exit()
        app_logger.info("SimpleFIN config validated.")
