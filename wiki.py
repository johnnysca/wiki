from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    #return handle_request()
    return front_page_request()


@app.route("/about")
def handle_request(name="wiki",content="stuff"):
    # TODO: load the desired page content
    return render_template(
        "main.html",
        page_name=name,
        page_content=content,
    )


@app.route("/view")
def front_page_request(wiki_name="Fedora's wiki"):
    with open("pages/FrontPage.txt", "r") as file:
        content = file.read()

    # TODO: load the desired page content
    return render_template(
        "main.html",
        page_name=wiki_name,
        page_content=content,
    )

#@app.route('/post/<int:post_id>')

@app.route("/view/<path:page_name>")
def page_request(page_name):
    try:
        with open("pages/" + str(page_name), "r") as file:
            content = file.read()
    except:
        raise FileNotFoundError 
    # TODO: load the desired page content
    return render_template(
        "main.html",
        page_name=page_name,
        page_content=content,
    )
