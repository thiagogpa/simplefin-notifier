# SimpleFin-Notifier 📢

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/thiagogpa/simplefin-notifier/build-docker-image.yml?label=Build%20Docker%20Image&logo=github&style=flat-square)](https://github.com/thiagogpa/simplefin-notifier/actions/workflows/build-docker-image.yml)
[![Docker Image Version](https://img.shields.io/docker/v/ghcr.io/thiagogpa/simplefin-notifier?label=Docker%20Image&logo=docker&style=flat-square)](https://github.com/thiagogpa/simplefin-notifier/pkgs/container/simplefin-notifier)
[![License](https://img.shields.io/github/license/thiagogpa/simplefin-notifier?style=flat-square)](https://github.com/thiagogpa/simplefin-notifier/blob/main/LICENSE)

SimpleFin-Notifier is a Python application that fetches data from the SimpleFIN API and sends notifications to various services like Discord, Telegram, ntfy, and Gotify. It's designed to be easily deployable using Docker and can be scheduled to run periodically using cron or a similar task scheduler.

## Features ✨

- 🔑 Securely stores and retrieves SimpleFIN API credentials
- 📡 Fetches data from the SimpleFIN API
- 📢 Sends notifications to Discord, Telegram, ntfy, and Gotify
- 🐳 Containerized using Docker for easy deployment
- 🔄 Can be scheduled to run periodically
- 🔒 Encrypts sensitive data using the `cryptography` library

## Getting Started 🚀

### Prerequisites

- Python 3.6 or higher
- Docker (optional, for containerized deployment)

### Installation

Clone the repository:

```bash
git clone https://github.com/thiagogpa/simplefin-notifier.git
cd SimpleFin-Notifier
```

### Configuration ⚙️

The application is configured using environment variables. 
You can set these variables in the .env file, based on the provided .env.template


### Docker Deployment

#### Docker Compose

Run the application via docker-compose

    docker compose up -d

#### Bulding the image


    docker build -t simplefin-notifier .


Then, run the Docker container:

    docker run -d --name simplefin-notifier --env-file .env simplefin-notifier


### Running Locally

1. Install the required Python packages:

   ```
   bash
   pip install -r requirements.txt
   ```

2. Run the application:

    ```
    python main.py   
    ```






### Full list of environment variables

- `CREDENTIALS_PATH`:	    Path to store the SimpleFIN credentials (default: ./credentials)
- `SIMPLEFIN_BRIDGE_TOKEN`:	The app token provided by SimpleFIN Bridge for authentication (required)
- `GOTIFY_BASE_URL`:	    Base URL for the Gotify server
- `GOTIFY_APP_TOKEN`:	    App token for the Gotify server
- `DISCORD_WEBHOOK_URL`:    Discord webhook URL for sending notifications
- `TELEGRAM_BOT_TOKEN`:	    Telegram bot token for sending notifications
- `TELEGRAM_CHAT_ID`:	    Telegram chat ID to send notifications to
- `NTFY_URL`:	            URL for the ntfy server including the topic
- `NTFY_TOKEN`:	            Token for the ntfy server if Authorization is required
- `NTFY_PRIORITY`:	        Priority level for the ntfy notification (default: 3)
- `ENCRYPTION_KEY`:	        Encryption key for securing sensitive data (generated automatically if not provided)


### Contributing 🤝

Contributions are welcome! Please feel free to open issues or submit pull requests for bug fixes, improvements, or new features.

### License 📄
This project is licensed under the MIT License.