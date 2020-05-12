from flask import Blueprint, render_template

from .models import Contest

NAME_APP = 'contests'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def contests_page():
    upcoming_contest = Contest.query.first()
    return render_template(f'{NAME_APP}/contests.html', title='Contests', contest=upcoming_contest)


@app.route('/contests-list')
def contests_list():
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Contests')


@app.route('/past-contests-list')
def past_contests_list():
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Past contests')


@app.route('/contest/item=<id>')
def contests_instance(id):
    contest = Contest.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Contests', item=contest)
