import pytest
import requests
import json

#url = "http://10.117.173.40:8080/v1/user/"

@pytest.mark.dependency()
def test_add_user(url):
    payload = {"id": "3", "name": "William", "gender": "male", "email": "william@clouddemo.com","phone": "12311212121"}
    r = requests.post(url, json=payload)
    assert r.status_code == 200

@pytest.mark.dependency(depends=["test_add_user"])
def test_get_user(url):
    r = requests.get(url+"3")
    assert r.status_code == 200
    assert r.json()["name"] == "William"

@pytest.mark.dependency(depends=["test_get_user"])
def test_delete_user(url):
    r = requests.delete(url+"3")
    assert r.status_code == 204