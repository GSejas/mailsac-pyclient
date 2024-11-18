import pytest
import os
from pymailsac.client import MailsacClient, MailsacException, EmailMessage

@pytest.fixture(scope="session")
def mail_test_email():
    return os.environ.get("MAILSAC_TEST_EMAIL") or "some@email.com"

@pytest.fixture(scope="session")
def mailsac_client():
    """
    Fixture to create and return a Mailsac client instance for the test session.

    This fixture retrieves the Mailsac API key from the environment variable 
    'MAILSAC_API_TOKEN'. If the environment variable is not set, it raises a 
    ValueError. The API key is then used to authenticate and create a Mailsac 
    client instance.

    Returns:
        Mailsac: An authenticated Mailsac client instance.

    Raises:
        ValueError: If the 'MAILSAC_API_KEY' environment variable is not set.
    """
    test_api_key = os.environ.get("MAILSAC_API_KEY")
    if not test_api_key:
        raise ValueError("MAILSAC_API_KEY environment variable not set")
    return MailsacClient(api_key=test_api_key)
