from flask import Blueprint, render_template

NAME_APP = 'cases'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def cases_page():
    return render_template(f'{NAME_APP}/cases_page.html', title='Cases')