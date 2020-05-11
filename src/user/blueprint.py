from flask import Blueprint, render_template
from .models import User

NAME_APP = 'users'

app = Blueprint(NAME_APP, __name__)


@app.route('/register')
def signup():
    pass
