import pytest
import requests
import json

url = "http://localhost:8080/v1/user/"

def test_add_get_delete_user():
    r = requests.get(url+"100")
    assert r.status_code == 200
    assert r.json()["name"] == "a23"

def test_add_user():
    params = {"1":"2"}
    assert 1 == 1