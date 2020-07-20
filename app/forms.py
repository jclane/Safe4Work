from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, url


class GetUrlForm(FlaskForm):
    address = StringField(render_kw={"placeholder": "Enter URL"}, validators=[DataRequired(), url()])
    submit_btn = SubmitField("Make S4W")
