from flask import Blueprint, render_template

NAME_APP = 'general'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def home_page():
    return render_template(f'{NAME_APP}/main.html', title='Home')
