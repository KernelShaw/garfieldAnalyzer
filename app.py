from flask import Flask, request, render_template
from strip_methods import GarfieldBase

# GLOBALS
RANDOM_STRIP = ""
GARFIELD_ANALYZER = GarfieldBase()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def garfield_analyzer():
    global RANDOM_STRIP
    global GARFIELD_ANALYZER

    if RANDOM_STRIP == "":
        RANDOM_STRIP = GARFIELD_ANALYZER.random_strip()
    strip_location = "/static/garfield/" + RANDOM_STRIP + ".gif"

    if request.method == "POST":
        selection = request.form.get("selection")
        if selection is None:
            return render_template('main.html', comic=strip_location, status_message="No selection. Please select one "
                                                                                     "of the joke options.")
        else:
            GARFIELD_ANALYZER.update_entry_details(RANDOM_STRIP, selection)
            RANDOM_STRIP = GARFIELD_ANALYZER.random_strip()
            strip_location = "/static/garfield/" + RANDOM_STRIP + ".gif"
            print("entry added")
            return render_template('main.html', comic=strip_location, status_message="Thanks for your response!"
                                                                                     " Keep going.")
    else:
        RANDOM_STRIP = GARFIELD_ANALYZER.random_strip()
        strip_location = "/static/garfield/" + RANDOM_STRIP + ".gif"

    return render_template('main.html', comic=strip_location)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__app__":
    app.run(host='192.168.1.185', debug=True)
