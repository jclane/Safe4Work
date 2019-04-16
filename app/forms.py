from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, url


class SearchForm(FlaskForm):
    address = StringField(render_kw={"placeholder": "Enter URL"}, validators=[DataRequired(), url()])
    submit = SubmitField("Make S4W")
