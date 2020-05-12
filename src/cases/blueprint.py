from flask import Blueprint, render_template

from .models import Case

NAME_APP = 'cases'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def cases_page():
    cases = Case.query.all()

    return render_template(f'{NAME_APP}/cases_page.html', title='Cases', cases=cases)
