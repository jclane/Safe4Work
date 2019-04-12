from flask import render_template, request

from app.make_it_safe import SafeArticle
from app.forms import SearchForm
from app import app

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SearchForm(request.form)
    if form.validate_on_submit():
        return render_template("index.html", title="BLAH", form=form, article=SafeArticle(request.form["address"]))
    return render_template("index.html", title="Home", form=form)
