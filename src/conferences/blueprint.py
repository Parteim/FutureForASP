from flask import Blueprint, render_template

NAME_APP = 'conferences'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def conferences_page():
    return render_template(f'{NAME_APP}/conferences.html', title='Conferences')
