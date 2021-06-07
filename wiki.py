from flask import Flask, request
from flask import render_template
import format
import json

app = Flask(__name__)


@app.route("/")
def main():
    return front_page_request()


# Example function, to be changed or deleted later
@app.route("/about")
def handle_request(name="wiki", content="stuff"):
    """
    Calls Render Template passing paramaters that map to properties of web page.

    Args:
        name: The name to be be displayed on the page title.
        content: Text displayed on the webpage when template is rendered.

    Returns:
        Rendered webpage containing the arguments, but displayed in plaintext.
    """
    return render_template(
        "main.html",
        page_name=name,
        page_content=content,
    )  # pragma: no cover


@app.route("/view")
def front_page_request():
    """Used by main to display the front page of wiki"""
    return page_request("FrontPage")


@app.route("/view/<path:page_name>")
def page_request(page_name: str) -> str:
    """
    Displays webpage from txt file

    Opens the text file that is requested according to its location in
    the wiki repository.  Reads the txt file, then it opens an html file
    with the desired contents to be displayed in a webpage.

    Args:
        page_name: Name of the txt that is being requested to view and name of html to be created

    Returns:
        Rendered webpage containing the arguments, but displayed in plaintext.

    Raises:
        FileNotFoundError: Flags when the txt file requested cant be found
    """
    try:
        with open("pages/" + str(page_name) + ".txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError

    with open("templates/" + str(page_name) + ".html", "w") as file:
        file.write(format.formatter(content))

    # Load the desired page content
    return render_template(page_name + ".html")


@app.route('/api/v1/page/<page_name>/get')
def page_api_get(page_name):
    f = request.args.get('format', 'all') # format is a dictionary
    json_response = {}
    status_code = 200
    # TODO: implement response
    if f == "all":
        with open("pages/" + str(page_name) + ".txt", "r") as file:
            content = file.read()
        h_content = format.formatter(content)
        json_response = {"success":True, "raw": content, "html": h_content}
    return json_response , status_code