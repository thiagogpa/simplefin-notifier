"""
Executes the main logic of the application, including setting up notifications and fetching data from the SimpleFIN API.

The `main()` function performs the following steps:
1. Sets up the notification service using the `NotificationSetup` class.
2. Sets up the SimpleFIN API credentials using the `SimpleFINCredentialSetup` class.
3. Fetches data from the SimpleFIN API using the `fetch_simplefin_data()` function.
4. If there are any errors in the SimpleFIN API response, it sends a notification with the error details.
5. If there are no errors, it logs a message indicating that no errors were found.
"""

from utils.init_logger import app_logger
from services.simplefin_service import fetch_simplefin_data
from setup.notification_setup import NotificationSetup
from setup.simplefin_setup import SimpleFINCredentialSetup


def main():
    notification_setup = NotificationSetup()
    notification_service = notification_setup.setup_notifications()

    simplefin_setup = SimpleFINCredentialSetup()
    simplefin_setup.setup_credentials()
    simplefin_data = fetch_simplefin_data()

    if simplefin_data["errors"]:
        error_message = "Errors from SimpleFIN API:\n"
        for error in simplefin_data["errors"]:
            error_message += f"- {error}\n"
        app_logger.info("Errors found in the SimpleFIN API response. Notifying user.")
        app_logger.debug(f"Error message: {error_message}")
        notification_service.notify(
            title="SimpleFIN Connection Issues",
            message=error_message,
            priority=0,
        )
    else:
        app_logger.info("No errors found in the SimpleFIN API response.")


if __name__ == "__main__":
    main()
