from flask import Blueprint, render_template

NAME_APP = 'ads'

app = Blueprint(NAME_APP, __name__)

@app.route('/ad')
def show_ad():
    return render_template(f'{NAME_APP}/instance.html')