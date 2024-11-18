import pytest
from pymailsac.client import MailsacClient, MailsacException
from dotenv import load_dotenv
import os
import logging
from unittest.mock import patch, Mock
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Retrieve the test API key from environment variables
test_api_key = "test_api_key"
mail_test_email = "test@testing.com"


@pytest.fixture
def client():
    return MailsacClient(api_key=test_api_key)




def test_get_messages_exception(client):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.text = "Internal Server Error"
        
        with pytest.raises(MailsacException, match="Failed to fetch messages: Internal Server Error"):
            client.get_messages(mail_test_email)

def test_get_message_exception(client):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = "Not Found"
        
        with pytest.raises(MailsacException, match="Failed to fetch message: Not Found"):
            client.get_message(mail_test_email, "invalid_message_id")

def test_delete_message_exception(client):
    with patch('requests.delete') as mock_delete:
        mock_delete.return_value.status_code = 403
        mock_delete.return_value.text = "Forbidden"
        
        with pytest.raises(MailsacException, match="Failed to delete message: Forbidden"):
            client.delete_message(mail_test_email, "invalid_message_id")

def test_check_health_exception(client):
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Health check failed")
        
        assert client.check_health() is False