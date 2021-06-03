"""Integration tests for app.py"""
import pytest

from bank_api.app import app
from flask import Response


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    
    #pass

    
    url = '/accounts/foo'
    post_result: Response = client.post(url)
    assert post_result.status_code == 200

    get_result: Response = client.get(url)
    assert get_result.status_code == 200


