from flask import Flask, request, render_template, redirect, url_for
from strip_methods import GarfieldBase

# GLOBALS
RANDOM_STRIP = ""
GARFIELD_ANALYZER = GarfieldBase()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def garfield_analyzer():
    global RANDOM_STRIP
    global GARFIELD_ANALYZER

    RANDOM_STRIP = GARFIELD_ANALYZER.random_strip()
    strip_location = "/static/garfield/" + RANDOM_STRIP + ".gif"

    if request.method == "POST":
        selection = request.form.get("selection")
        if selection is None:
            return render_template('main.html', comic=strip_location, status_message="No selection. Please select one "
                                                                                     "of the joke options.")
        else:
            GARFIELD_ANALYZER.update_entry_details(RANDOM_STRIP, selection)
            return redirect(url_for('garfield_redirect'))
    else:
        return render_template("main.html", comic=strip_location)


@app.route("/success", methods=["GET", "POST"])
def garfield_redirect():
    global RANDOM_STRIP
    global GARFIELD_ANALYZER

    RANDOM_STRIP = GARFIELD_ANALYZER.random_strip()
    strip_location = "/static/garfield/" + RANDOM_STRIP + ".gif"

    if request.method == "POST":
        selection = request.form.get("selection")
        if selection is None:
            return render_template('main.html', comic=strip_location, status_message="No selection. Please select one "
                                                                                     "of the joke options.")
        else:
            GARFIELD_ANALYZER.update_entry_details(RANDOM_STRIP, selection)
            return redirect(url_for('garfield_redirect'))

    return render_template("main.html", comic=strip_location, status_message="Thanks for your response!")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/examples")
def joke_examples():
    return render_template('joke_explanations.html')


@app.route("/odie")
def odie():
    joke = "Garfield hates Odie?"
    text = "This is Odie! He's Jon's dog. Select this option for any strip where the humor is derived from" \
           " Garfield's abuse of or distaste for Odie."
    return render_template('joke.html',
                           s1="static/example_strips/od1.png",
                           s2="static/example_strips/od2.jpeg",
                           s3="static/example_strips/od3.webp",
                           joke=joke,
                           explanation=text,
                           example_image="static/example_characters/odie.png")


@app.route("/irma")
def irma():
    joke = "Irma joke?"
    text = "This is Irma! She's a waitress at the local coffee shop." \
           " Select this category for any strip where the main joke is Irma being bad at her job."
    return render_template('joke.html',
                           s1="static/example_strips/i1.gif",
                           s2="static/example_strips/i2.webp",
                           s3="static/example_strips/i3.gif",
                           joke=joke,
                           explanation=text,
                           example_image="static/example_characters/irma.webp")


@app.route("/nermal")
def nermal():
    joke = "Garfield hates Nermal?"
    text = "This is Nermal! He's a cat Garfield can't stand. Select this category for " \
           "any strip where the humor is derived from Garfield hating Nermal."
    return render_template('joke.html',
                           s1="static/example_strips/n1.webp",
                           s2="static/example_strips/n2.jpeg",
                           s3="static/example_strips/n3.webp",
                           joke=joke,
                           explanation=text,
                           example_image="static/example_characters/nermal.png")


@app.route("/arlene")
def arlene():
    joke = "Garfield and Arlene?"
    text = "This is Arlene! She's Garfield's girlfriend. Select this option for any strip where" \
           " the joke is based around Arlene."
    return render_template('joke.html',
                           s1="static/example_strips/a1.webp",
                           s2="static/example_strips/a2.webp",
                           s3="static/example_strips/a3.webp",
                           joke=joke,
                           explanation=text,
                           example_image="static/example_characters/arlene.webp")


@app.route("/spiders")
def spiders():
    joke = "Garfield hates spiders?"
    text = "Garfield hates spiders. This comes up a lot."
    return render_template('joke.html',
                           s1="static/example_strips/sp1.webp",
                           s2="static/example_strips/sp2.jpeg",
                           s3="static/example_strips/sp3.png",
                           joke=joke,
                           explanation=text)


@app.route("/relate")
def relate():
    joke = "Relatable humor?"
    text = "\"I Hate Mondays\" anybody? Select this option for any strip that can be classified as " \
           "\"relatable humor\". If the strip's joke has you saying \"Yeah, that's totally me,\" it's relatable " \
           "humor."
    return render_template('joke.html',
                           s1="static/example_strips/r1.gif",
                           s2="static/example_strips/r2.gif",
                           s3="static/example_strips/r3.gif",
                           joke=joke,
                           explanation=text)


@app.route("/surreal")
def surreal():
    joke = "Surreal/Absurdist?"
    text = "Surreal humor is hard to define. Please look at the examples below to get a feel for it."
    return render_template('joke.html',
                           s1="static/example_strips/s1.gif",
                           s2="static/example_strips/s2.gif",
                           s3="static/example_strips/s3.gif",
                           joke=joke,
                           explanation=text)


@app.route("/fat")
def fat():
    joke = "Garfield is Lazy/Gluttonous?"
    text = "Garfield is fat. Garfield is lazy. A little self-explanatory, no?"
    return render_template('joke.html',
                           s1="static/example_strips/l1.gif",
                           s2="static/example_strips/l2.jpeg",
                           s3="static/example_strips/l3.jpeg",
                           joke=joke,
                           explanation=text)


@app.route("/jon_sad")
def jon_sad():
    joke = "Jon is pathetic?"
    text = "According to current data on the subject, the most common Garfield joke is probably 'Haha, Jon " \
           "is pathetic.' This might come as a surprise to most of you. Select this option for any strip where " \
           "the joke comes entirely at the expense of Jon."
    return render_template('joke.html',
                           s1="static/example_strips/jp1.gif",
                           s2="static/example_strips/jp2.gif",
                           s3="static/example_strips/jp3.gif",
                           joke=joke,
                           explanation=text)


@app.route("/gar_hurt_jon")
def gar_hurt_jon():
    joke = "Garfield abusing Jon?"
    text = "Garfield tortures Jon. Like, a lot. If the strip's joke is that Garfield makes Jon's life just that much " \
           "more difficult, select this option."
    return render_template('joke.html',
                           s1="static/example_strips/gj1.gif",
                           s2="static/example_strips/gj2.gif",
                           s3="static/example_strips/gj3.gif",
                           joke=joke,
                           explanation=text)


@app.route("/other")
def other():
    joke = "Other?"
    text = "Do not be alarmed if you answer \"Other\" for a lot of these strips. They account for roughly 17% of\"" \
           " the comic's jokes (using the previous smaller subset of 1000 strips). Use this category for anything from " \
           "running jokes to jokes that amount to 'Haha, Garfield is a cat. Cats don't do that!'"
    return render_template('joke.html',
                           s1="static/example_strips/o1.gif",
                           s2="static/example_strips/o2.gif",
                           s3="static/example_strips/o3.gif",
                           joke=joke,
                           explanation=text)


if __name__ == "__app__":
    app.run(host='192.168.1.185', debug=True)
