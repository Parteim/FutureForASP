from flask import Blueprint, render_template

NAME_APP = 'contests'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def contests_page():
    return render_template(f'{NAME_APP}/contests.html', title='Contests')

@app.route('/contests-list')
def contests_list():
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Contests')

@app.route('/past-contests-list')
def past_contests_list(id):
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Past contests')

@app.route('/contest/item=<id>')
def contests_instance(id):
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Contests')


