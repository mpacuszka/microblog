from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Mateusz"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        },
        {
            "author": {"username": "Susan"},
            "body": """
            You can spell check very long text areas without compromising any performance hits. 
            Regardless of the size of the text, UltimateSpell only sends small portions of the text to the server as needed, while the user spell checks through the text.

            Basically the spell check dialog box makes on-demand calls to a callback page on the server without refreshing the whole page or dialog. 
            It keeps processing small blocks of text using the AJAX (Asynchronous JavaScript and XML) techniques.

            Note that UltimateSpell displays the text in the dialog box sentence-by-sentence just like Microsoft Word. 
            This helps the user understand the actual context in which the spelling error occurs.
            """
        }
    ]
    return render_template("index.html", title="Home Page", user=user, posts=posts)
