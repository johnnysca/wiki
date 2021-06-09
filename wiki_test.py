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


def test_edit_page(client):
    resp = client.get("/edit/PageName")

    assert 200 == resp.status_code


def test_error_message_404(client):
    resp = client.get("/view/NoPageFound")

    assert b"<!DOCTYPE html>" in resp.data
    assert b"<h1>Error 404 Page Not Found</h1>" in resp.data
    assert (
        b'<p>Page can be created <a href="/edit/NoPageFound">here</a></p>' in resp.data
    )


def test_save_page_edits():
    wiki.save_page_edits("Test_log", "John Doe", "john@doe.com", "some changes here.")
    with open("history_log/Test_log.log") as f:
        contents = f.read()
    assert "John Doe" in contents
    assert "john@doe.com" in contents
    assert "some changes here." in contents


"""
The tests below do not work in Git Lab because the
created files are ignored. They should, however
work on a local device.
"""


# def test_load_logs():
# expected = [
#     {
#         "Time": "2021-06-09 14:36:12.919747",
#         "Name": "Jane Doe",
#         "Email": "jane@doe.com",
#         "Change Description": "some change",
#     },
#     {
#         "Time": "2021-06-09 14:39:41.279648",
#         "Name": "John Doe",
#         "Email": "john@doe.com",
#         "Change Description": "some change",
#     },
# ]
# output = wiki.load_page_logs("TestPageLog")

# assert output == expected


# def test_view_page_history(client):
#     resp = client.get("/history/TestPageLog")

#     assert b"Jane Doe" in resp.data
#     assert b"John Doe" in resp.data
#     assert b"jane@doe.com" in resp.data
#     assert b"john@doe.com" in resp.data
#     assert b"some change" in resp.data
#     assert b"2021-06-09 14:36:12.91974" in resp.data
#     assert b"2021-06-09 14:39:41.279648" in resp.data

#     assert resp.status_code == 200
