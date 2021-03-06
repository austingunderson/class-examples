from datetime import date

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField, EmailField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')


# Simple form handling using raw HTML forms
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        first_name = request.form['firstname']
        last_name = request.form['lastname']

        # Validate form data
        if len(first_name) == 0 or len(last_name) == 0:
            # Form data failed validation; try again
            error = "Please supply both first and last name"
        else:
            # Do other business logic here!
            # Form data is valid; move along
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('sign-up.html', message=error)


# Two buttons!
@app.route('/two-buttons', methods=['GET', 'POST'])
def two_buttons():
    if request.method == 'POST':
        print "Action is {}".format(request.form['action'])
    return render_template('two-buttons.html')


# More powerful approach using WTForms
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')


# More powerful approach using WTForms
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return redirect(url_for('thank_you'))

    return render_template('register.html', form=form, message=error)


# HTML5 Inputs
class HTML5InputsForm(FlaskForm):
    start_date = DateField('Start Date', default=date.today())
    email_addr = EmailField('E-Mail Address')


@app.route('/html5-inputs', methods=['GET', 'POST'])
def html5_inputs():
    html5_form = HTML5InputsForm()
    return render_template('html5-inputs.html', form=html5_form)


# Run the application
app.run(debug=True)
