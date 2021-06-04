from flask import Flask
from flask import render_template
import format

app = Flask(__name__)


@app.route("/")
def main():
    return front_page_request()


# Example function, to be changed or deleted later
@app.route("/about")
def handle_request(name="wiki", content="stuff"):
    # TODO: load the desired page content
    return render_template(
        "main.html",
        page_name=name,
        page_content=content,
    )


@app.route("/view")
def front_page_request():
    return page_request("FrontPage")


@app.route("/view/<path:page_name>")
def page_request(page_name):
    try:
        with open("pages/" + str(page_name) + ".txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError

    with open("templates/" + str(page_name) + ".html", "w") as file:
        file.write(format.formatter(content))

    # Load the desired page content
    return render_template(page_name + ".html")
