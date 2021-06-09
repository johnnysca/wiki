# import pathlib
import pytest  # type:ignore
import wiki


# TODO: add more comments after docstring clarification


@pytest.fixture
def client():
    # Arrange
    wiki.app.config["TESTING"] = True

    # act
    with wiki.app.test_client() as client:
        yield client


def test_import():
    # Assert
    assert wiki is not None


# TODO: update test to something consistent for our test directory
def test_homepage(client):
    # Assign
    resp = client.get("/")

    # Assert
    assert resp.status_code == 200
    assert resp.data is not None


def test_page_name(client):
    # Assign
    resp = client.get("/view/PageName")

    # Assert
    assert resp.status_code == 200
    assert resp.data is not None


def test_empty_page_name(client):
    """Tests file not found error"""

    # Assert
    # with pytest.raises(FileNotFoundError):
    # client.get("/view/<TMNT>")
    response = client.get("/view/<TMNT>")
    assert response.status_code == 404


def test_view_page_name(client):
    # Assign
    resp = client.get("/view/test_pages/name_test")

    # Assert
    assert resp.status_code == 200
    assert b"Geidel\nKevin\nJohnny" in resp.data


def test_formatting(client):
    """Tests if marko input is properly converted"""
    # Assign
    resp = client.get("/view/test_pages/testing")

    # Assert
    assert b"<h1>Happy Late Memorial Day</h1>" in resp.data
    assert b"<p>It was a great <strong>day</strong></p>" in resp.data
    assert b"<p>Memorial day is a day to celebrate</p>" in resp.data
    assert (
        b'<a href="https://images.app.goo.gl/cF4oaTNxEPsMFKk76">Memorial day picture</a>'
        in resp.data
    )
