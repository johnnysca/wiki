import pathlib

import pytest



import wiki




@pytest.fixture
def client():
    wiki.app.config["TESTING"] = True

    with wiki.app.test_client() as client:
        yield client


def test_import():
    assert wiki is not None

#TODO: update hello world to something consistent for our test directory
def test_homepage(client):
    resp = client.get("/")
    assert resp.status_code == 200
    #assert b"Hello, World!\n" in resp.data

def test_empty_page_name(client):
    with pytest.raises(FileNotFoundError) as e:
        resp = client.get("/view/<TMNT>")

def test_view_page_name(client):
 
    resp = client.get("/view/test_pages/name_test.txt")

    assert b"Geidel\nKevin\nJohnny" in resp.data


