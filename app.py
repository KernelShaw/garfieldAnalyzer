from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def garfield_analyzer():
    random_strip = "/static/strips/" + str(random.randint(1, 3)) + ".gif"
    return render_template('main.html', comic=random_strip)
    #return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return render_template('test.html', name="Felix")
    #return "<p>1</p>"


if __name__ == "__app__":
    app.run(host="127.0.0.1", port=8080, debug=True)
