import logging
import os
from unittest.mock import patch, Mock
import pytest
from pymailsac.client import MailsacClient, MailsacException, EmailMessage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def client():
    api_key = "test_api_key"
    return MailsacClient(api_key)


@patch('requests.get')
def test_get_message(mock_get, client):
    mail_test_email = "demoaddress@mailsac.com"
    test_message_id = "hgu4LTZkvkQvKbsHwbOwjkLmgM-0"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "_id": "hgu4LTZkvkQvKbsHwbOwjkLmgM-0",
        "from": [
          {
            "address": "demoaddress@mailsac.com",
            "name": "Demo Account"
          }
        ],
        "to": [
          {
            "address": "hellohellohola@mailsac.com",
            "name": ""
          }
        ],
        "cc": [],
        "bcc": [],
        "subject": "Speed Test",
        "savedBy": None,
        "inbox": "hellohellohola@mailsac.com",
        "originalInbox": "hellohellohola@mailsac.com",
        "domain": "mailsac.com",
        "received": "2023-01-25T23:20:21.736Z",
        "size": 4324,
        "attachments": [],
        "ip": "204.62.115.202",
        "via": "172.31.27.141",
        "folder": "inbox",
        "labels": [],
        "read": None,
        "rtls": True,
        "links": [],
        "spam": 0
      }
    
    mock_get.return_value = mock_response

    logger.info("Starting test_get_message")
    response = client.get_message(mail_test_email, test_message_id)
    logger.info("Received response: %s", response)
    assert isinstance(response, EmailMessage)
    assert response.id == test_message_id
    logger.info("test_get_message passed")


@patch('requests.get')
def test_get_message_plain_text(mock_get, client):
    mail_test_email = "test@example.com"
    test_message_id = "test_message_id"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "Test message content"
    mock_get.return_value = mock_response

    logger.info("Starting test_get_message_plain_text")
    response = client.get_message_plain_text(mail_test_email, test_message_id)
    logger.info("Received response: %s", response)
    assert isinstance(response, str)
    assert response == "Test message content"
    logger.info("test_get_message_plain_text passed")


@patch('requests.delete')
def test_delete_message(mock_delete, client):
    mail_test_email = "test@example.com"
    test_message_id = "test_message_id"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_delete.return_value = mock_response

    logger.info("Starting test_delete_message")
    response = client.delete_message(mail_test_email, test_message_id)
    logger.info("Received response: %s", response)
    assert response is True
    logger.info("test_delete_message passed")


@patch('requests.delete')
def test_delete_messages(mock_delete, client):
    mail_test_email = "test@example.com"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_delete.return_value = mock_response

    logger.info("Starting test_delete_messages")
    response = client.delete_messages(mail_test_email)
    logger.info("Received response: %s", response)
    assert response is True
    logger.info("test_delete_messages passed")


@patch('requests.get')
def test_check_health(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    logger.info("Starting test_check_health")
    response = client.check_health()
    logger.info("Received response: %s", response)
    assert response is True
    logger.info("test_check_health passed")
