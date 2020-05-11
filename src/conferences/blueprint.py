from flask import Blueprint, render_template

NAME_APP = 'conferences'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def conferences_page():
    return render_template(f'{NAME_APP}/conferences.html', title='Conferences')

@app.route('/conferences-list')
def conferences_list():
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Conferences')

@app.route('/past-conferences-list')
def past_conferences_list():
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Past conferences')

@app.route('/conferences/item=<id>')
def conferences_instance(id):
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Conferences')