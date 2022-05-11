from flask import Flask, request, render_template
import random
from strip_methods import GarfieldBase

# GLOBALS
RANDOM_STRIP = ""
GARFIELD_ANALYZER = GarfieldBase
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def garfield_analyzer():
    global RANDOM_STRIP

    if RANDOM_STRIP == "":
        RANDOM_STRIP = "/static/strips/" + str(random.randint(1, 3)) + ".gif"

    if request.method == "POST":
        selection = request.form.get("selection")
        if selection is None:
             # Return new HTML page, DO NOT UPDATE COMIC VAR
        else:
            decoy_method(selection)  # Database edits
            RANDOM_STRIP = "/static/strips/" + str(random.randint(1, 3)) + ".gif"
    else:
        RANDOM_STRIP = "/static/strips/" + str(random.randint(1, 3)) + ".gif"

    return render_template('main.html', comic=RANDOM_STRIP)


@app.route("/about")
def about():
    return render_template('test.html', name="Felix")
    #return "<p>1</p>"


if __name__ == "__app__":
    app.run(host="127.0.0.1", port=8080, debug=True)
