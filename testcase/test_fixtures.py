import requests
import pytest

@pytest.fixture()
def topics():
    return requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()

def test_1(topics):
    assert len(topics["topics"]) == 2

def test_2(topics):
    assert topics["topics"][0]["deleted"] == False