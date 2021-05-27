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

#TODO: update test to something consistent for our test directory
def test_homepage(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data is not None

def test_page_name(client):
    resp = client.get("/view/PageName")
    assert resp.status_code == 200
    assert resp.data is not None

def test_empty_page_name(client):
    with pytest.raises(FileNotFoundError) as e:
        resp = client.get("/view/<TMNT>")

def test_view_page_name(client):
    resp = client.get("/view/test_pages/name_test")
    assert resp.status_code == 200
    assert b"Geidel\nKevin\nJohnny" in resp.data