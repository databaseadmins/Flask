from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root_page():
    return "Hello from the root"


@app.route("/expressions/")
def hello_world():
    name="Coleman"
    age=24
    career="Real estate mogul"
    template_name="Jinja2"

    kwargs = {
        "name" : name,
        "age" : age,
        "career" : career,
        "template_name" : template_name
    }
    return render_template(
        "jinja_intro.html", **kwargs
        )

