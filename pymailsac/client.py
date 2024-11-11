"""
# Mailsac Client

This module provides a client for interacting with the Mailsac API. It 
includes methods for fetching, deleting, and checking the health of email messages.

## Classes
- `MailsacException`: Custom exception for Mailsac errors.
- `MailsacClient`: Client for interacting with the Mailsac API.

## Usage
"""

import requests
from typing import List
from .schemas import EmailMessage


class MailsacException(Exception):
    """Custom exception for Mailsac errors."""

    pass


class MailsacClient:
    """
    Client for interacting with the Mailsac API.

    Attributes:
        api_key (str): The API key for authenticating with the Mailsac API.
        base_url (str): The base URL for the Mailsac API.
        headers (dict): The headers to include in API requests.
    """

    def __init__(self, api_key: str, base_url: str = "https://mailsac.com/api"):
        """
        Initializes the MailsacClient with the provided API key and base URL.

        Args:
            api_key (str): The API key for authenticating with the Mailsac API.
            base_url (str, optional): The base URL for the Mailsac API.
            Defaults to "https://mailsac.com/api".
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Mailsac-Key": self.api_key, "Content-Type": "application/json"}

    def get_messages(self, email: str) -> List[EmailMessage]:
        """
        Fetches messages for a specified email address.

        Args:
            email (str): The email address to fetch messages for.

        Returns:
            List[EmailMessage]: A list of email messages.

        Raises:
            MailsacException: If the request to fetch messages fails.
        """
        response = requests.get(
            f"{self.base_url}/addresses/{email}/messages",
            headers=self.headers,
            timeout=10,
        )
        if response.status_code != 200:
            raise MailsacException(f"Failed to fetch messages: {response.text}")

        messages = response.json()
        return [EmailMessage(**msg) for msg in messages]

    def get_message(self, email: str, message_id: str) -> EmailMessage:
        """
        Fetches a single message by ID.

        Args:
            email (str): The email address to fetch the message for.
            message_id (str): The ID of the message to fetch.

        Returns:
            EmailMessage: The fetched email message.

        Raises:
            MailsacException: If the request to fetch the message fails.
        """
        response = requests.get(
            f"{self.base_url}/addresses/{email}/messages/{message_id}",
            headers=self.headers,
        )
        if response.status_code != 200:
            raise MailsacException(f"Failed to fetch message: {response.text}")

        return EmailMessage(**response.json())

    def delete_message(self, email: str, message_id: str) -> bool:
        """
        Deletes a message by ID.

        Args:
            email (str): The email address to delete the message for.
            message_id (str): The ID of the message to delete.

        Returns:
            bool: True if the message was successfully deleted, False otherwise.

        Raises:
            MailsacException: If the request to delete the message fails.
        """
        response = requests.delete(
            f"{self.base_url}/addresses/{email}/messages/{message_id}",
            headers=self.headers,
        )
        if response.status_code != 200:
            raise MailsacException(f"Failed to delete message: {response.text}")

        return response.status_code == 204

    def check_health(self) -> bool:
        """
        Verifies the health of the connection to the Mailsac server.

        Returns:
            bool: True if the connection is healthy, False otherwise.
        """
        try:
            # Perform a simple GET request to the base URL or
            # an endpoint that does not modify data
            response = requests.get(f"{self.base_url}/addresses", headers=self.headers)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Health check failed: {e}")
            return False
