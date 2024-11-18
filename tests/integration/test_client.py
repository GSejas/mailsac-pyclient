import pytest
from pymailsac.client import MailsacClient
import os
import logging

# import sib_api_v3_sdk

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def test_get_messages(mailsac_client, mail_test_email):
    # Retrieve the test API key from environment variables
    logger.debug("MAILSAC_TEST_EMAIL: %s", mail_test_email)  # Add this line
    logger.info("Starting test_get_messages")
    response = mailsac_client.get_messages(mail_test_email)
    logger.info("Received response: %s", response)
    assert isinstance(response, list)
    logger.info("test_get_messages passed")
    for rvd in response:
        response = mailsac_client.get_message(mail_test_email, rvd.id)
        assert response.subject == "Test Email For Testing"
        logger.info("Received response: %s", response)
        response = mailsac_client.get_message_plain_text(mail_test_email, rvd.id)
        logger.info("Received response: %s", response)
        assert response == 'Very testy\n\nJorge\n'


def test_check_health(mailsac_client):
    logger.info("Starting test_check_health")
    health_status = mailsac_client.check_health()
    logger.info("Health check status: %s", health_status)
    assert health_status is True
    logger.info("test_check_health passed")
    
