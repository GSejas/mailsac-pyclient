import pytest
from pymailsac.client import MailsacClient, MailsacException
from dotenv import load_dotenv
import os
import logging
from unittest.mock import patch, Mock

import sib_api_v3_sdk

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# configuration = sib_api_v3_sdk.Configuration()
# configuration.api_key["api-key"] = os.getenv("SIB_API_KEY")

# api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
#     sib_api_v3_sdk.ApiClient(configuration)
# )



@pytest.fixture
def client():
    test_api_key = os.getenv("MAILSAC_API_KEY")
    return MailsacClient(api_key=test_api_key)


def test_get_messages(client):
    # Retrieve the test API key from environment variables
    mail_test_email = os.getenv("MAILSAC_TEST_EMAIL")
    logger.debug("MAILSAC_TEST_EMAIL: %s", mail_test_email)  # Add this line
    logger.info("Starting test_get_messages")
    response = client.get_messages(mail_test_email)
    logger.info("Received response: %s", response)
    assert isinstance(response, list)
    logger.info("test_get_messages passed")
    for rvd in response:
        response = client.get_message(mail_test_email, rvd.id)
        assert response.subject == "Test Email For Testing"
        logger.info("Received response: %s", response)


def test_check_health(client):
    logger.info("Starting test_check_health")
    health_status = client.check_health()
    logger.info("Health check status: %s", health_status)
    assert health_status is True
    logger.info("test_check_health passed")

