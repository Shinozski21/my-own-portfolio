from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
import pandas as pd
import datetime


app = Flask(__name__)

current_year = datetime.datetime.now().year


@app.route("/")
def home():

    return render_template("index.html", year=current_year)
    debug = True


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html", year=current_year)

  #   if request.method == 'POST':
  #       if form.validate() == False:
  #           flash('All fields are required.')
  #           return render_template('contact4.html', form=form)
  #       else:
  #           msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
  #           msg.body = """
  # From: %s <%s>
  # %s
  # """ % (form.name.data, form.email.data, form.message.data)
  #           mail.send(msg)
  #           return 'Form posted.'
  #   elif request.method == 'GET':
  #       return render_template('contact4.html', form=form)
  #
  #
form = ContactForm()



@app.route("/resume")
def resume():
    return render_template("resume.html", year=current_year)


@app.route("/blog")
def blog():
    return render_template("blog.html", year=current_year)



@app.route("/about")
def about():
    return render_template("about.html", year=current_year)


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", year=current_year)


if __name__ == '__main__':
    app.run(debug=True)