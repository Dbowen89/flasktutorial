from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Name is required")])
    email = StringField("Email", validators=[DataRequired(message="Email is required"), Email(message="Please enter a valid email address.", check_deliverability=True)])
    subject = StringField("Subject", validators=[DataRequired(message="Subject is required")])
    message = TextAreaField("Message", validators=[DataRequired(message="Message is required")])
    submit = SubmitField("Send")
