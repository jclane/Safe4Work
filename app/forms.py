from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, url


class SearchForm(FlaskForm):
    address = StringField(validators=[DataRequired(), url()])
    submit = SubmitField("Make SFW")
