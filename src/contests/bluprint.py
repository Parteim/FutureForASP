from flask import Blueprint, render_template

NAME_APP = 'contests'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def contests_page():
    return render_template('contests/contests.html', title='Contests')
