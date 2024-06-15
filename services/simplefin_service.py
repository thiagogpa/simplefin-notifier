import json
import os
import requests
from cryptography.fernet import Fernet
from config.env_config import CREDENTIALS_PATH, ENCRYPTION_KEY

# Initialize Fernet with the encryption key
fernet = Fernet(ENCRYPTION_KEY.encode())


def fetch_simplefin_data():
    # Load and decrypt SimpleFIN credentials
    auth_file_path = os.path.join(CREDENTIALS_PATH, "simplefin_auth.json")

    if not os.path.exists(auth_file_path):
        raise FileNotFoundError(
            f"The credentials file '{auth_file_path}' does not exist."
        )

    with open(auth_file_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data).decode()
    sf_auth = json.loads(decrypted_data)

    # Fetch data from SimpleFIN
    res = requests.get(sf_auth["url"], auth=(sf_auth["username"], sf_auth["password"]))
    data = res.json()

    return data
