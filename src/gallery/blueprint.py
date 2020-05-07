from flask import Blueprint, render_template

NAME_APP = 'gallery'

app = Blueprint(NAME_APP, __name__)

@app.route('/')
def gallery_page():
    return render_template(f'{NAME_APP}/gallery_page.html', title='Gallery')