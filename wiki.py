from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    return handle_request()

@app.route("/about")
def handle_request(name="wiki",content="stuff"):
    # TODO: load the desired page content
    return render_template(
        "main.html",
        page_name=name,
        page_content=content,
    )