from flask import Blueprint, render_template
from flask_security import login_required

NAME_APP = 'forum'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
@login_required
def forum_page():
    return render_template(f'{NAME_APP}/forum_page.html', title='Forum')


@app.route('/create-post/')
@login_required
def create_post():
    pass


@app.route('/edit-post/<id>')
@login_required
def edit_post():
    pass
