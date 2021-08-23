from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, InputRequired
from modules import get_predicton

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'MyCode'

# Flask-Bootstrap requires this line
Bootstrap(app)


# with Flask-WTF, each web form is represented by a class
# "NameForm" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
class NameForm(FlaskForm):
    name = StringField('Please type your comment here', validators=[InputRequired()])
    submit = SubmitField('Submit')


# all Flask routes below

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    message = ""

    if form.validate_on_submit():
        name = form.name.data

        if get_predicton(name) == 0:
            message = "Positive Comment!"


        elif get_predicton(name) == 1:

            message = "Negative Comment!"
    return render_template('index.html', form=form, message=message)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
