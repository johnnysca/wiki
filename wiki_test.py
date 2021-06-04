# import pathlib
import pytest
import wiki


@pytest.fixture
def client():
    wiki.app.config["TESTING"] = True

    with wiki.app.test_client() as client:
        yield client


def test_import():
    assert wiki is not None


# TODO: update test to something consistent for our test directory
def test_homepage(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data is not None


def test_page_name(client):
    resp = client.get("/view/PageName")
    assert resp.status_code == 200
    assert resp.data is not None


def test_empty_page_name(client):
    with pytest.raises(FileNotFoundError):
        client.get("/view/<TMNT>")


def test_view_page_name(client):
    resp = client.get("/view/test_pages/name_test")
    assert resp.status_code == 200
    assert b"Geidel\nKevin\nJohnny" in resp.data


def test_formatting(client):
    resp = client.get("/view/test_pages/testing")
    assert b"<h1>Happy Late Memorial Day</h1>" in resp.data
    assert b"<p>It was a great <strong>day</strong></p>" in resp.data
    assert b"<p>Memorial day is a day to celebrate</p>" in resp.data
    assert (
        b'<a href="https://images.app.goo.gl/cF4oaTNxEPsMFKk76">Memorial day picture</a>'
        in resp.data
    )
