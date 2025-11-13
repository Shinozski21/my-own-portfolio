from wtforms import StringField, TextAreaField, SubmitField, Form
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm


class ContactForm(Form):
    name = StringField("Name",  validators=[DataRequired(message="Please enter your name.")])
    email = StringField("Email", validators=[DataRequired(message="Please enter your email address")])
    subject = StringField("Subject", validators=[DataRequired(message="Please enter a subject.")])
    message = TextAreaField("Message", validators=[DataRequired(message="Please enter a message.")])
    submit = SubmitField("Send")
