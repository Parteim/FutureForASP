from flask import Blueprint, render_template

NAME_APP = 'forum'
app = Blueprint(NAME_APP, __name__)

@app.route('/')
def forum_page():
    return render_template(f'{NAME_APP}/forum_page.html', title='Forum')