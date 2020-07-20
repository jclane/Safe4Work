from flask import render_template, request

from app.make_it_safe import SafeArticle
from app.forms import GetUrlForm
from app import app

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = GetUrlForm(request.form)
    if form.validate_on_submit():
        return render_template("index.html", title="Safe4Work - Article", form=form, article=SafeArticle(request.form["address"].strip()))

    return render_template("index.html", title="Safe4Work", form=form)
