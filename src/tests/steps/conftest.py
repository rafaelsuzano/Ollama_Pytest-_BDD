import pytest

@pytest.fixture
def user_payload():
    return {
        "username": "valid_user",
        "password": "valid_password",
        "email": "valid_user@example.com"
    }