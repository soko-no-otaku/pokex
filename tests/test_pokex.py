import os
import pytest
from flask.testing import Client
from functions_framework import create_app


@pytest.fixture
def client() -> Client:
    # cf. https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/functions/helloworld/sample_http_test_integration.py
    target = "pokex"
    source = os.path.join(os.path.dirname(__file__), "../main.py")
    with create_app(target, source).test_client() as client:
        yield client


def test_given_no_url_then_runtime_error_is_raised(client: Client):
    response = client.get("/")
    assert response.status_code == 500


def test_when_accessed_from_pocket_and_url_is_x_then_ogp_is_returned(client: Client):
    response = client.get(
        "/",
        query_string={"url": "https%3A%2F%2Fx.com%2Fexample%2Fstatus%2F99999999"},
        headers={
            "User-Agent": "PocketParser/2.0 (+https://getpocket.com/pocketparser_ua)"
        },
    )
    assert response.status_code == 200
    assert "<title>@example</title>" in response.get_data(as_text=True)


def test_when_accessed_from_pocket_and_url_is_not_x_then_redirected(client: Client):
    response = client.get(
        "/",
        query_string={"url": "https%3A%2F%2Fexample.com%2F"},
        headers={
            "User-Agent": "PocketParser/2.0 (+https://getpocket.com/pocketparser_ua)"
        },
    )
    assert response.status_code == 302
    assert response.location == "https://example.com/"


def test_when_accessed_from_browser_and_url_is_x_then_redirected(client: Client):
    response = client.get(
        "/",
        query_string={"url": "https%3A%2F%2Fx.com%2Fexample%2Fstatus%2F99999999"},
        headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        },
    )
    assert response.status_code == 302
    assert response.location == "https://x.com/example/status/99999999"


def test_when_accessed_from_browser_and_url_is_not_x_then_redirected(client: Client):
    response = client.get(
        "/",
        query_string={"url": "https%3A%2F%2Fexample.com%2F"},
        headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        },
    )
    assert response.status_code == 302
    assert response.location == "https://example.com/"
