from flask import Blueprint, render_template
from datetime import datetime

from .models import Contest

NAME_APP = 'contests'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def contests_page():
    contests = Contest.query
    upcoming_contest = contests.first()
    past_contest = []
    for i in contests:
        print(i.end < datetime.now().date())
        print(i.end, datetime.now().date())
        if i.end < datetime.now().date():
            past_contest.append(i)
            print(i)

    return render_template(f'{NAME_APP}/contests.html', title='Contests', u_cont=upcoming_contest, p_cont=past_contest)


@app.route('/contests-list')
def contests_list():
    contests = Contest.query.all()
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Contests', items=contests)


@app.route('/past-contests-list')
def past_contests_list():
    contests = Contest.query.all()
    past_contest = []
    for i in contests:
        if i.end < datetime.now().date():
            past_contest.append(i)

    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Past contests', items=past_contest)


@app.route('/contest/item=<id>')
def contests_instance(id):
    contest = Contest.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Contests', item=contest)
