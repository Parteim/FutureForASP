from flask import Blueprint, render_template
from datetime import datetime
from sqlalchemy import desc

from .models import WorldSkillsContest

NAME_APP = 'world_skills'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def world_skills_page():
    contest = WorldSkillsContest.query.order_by(desc(WorldSkillsContest.date)).first()
    past_contest = None
    for i in WorldSkillsContest.query.all():
        if i.date < datetime.now().date():
            past_contest = i
    return render_template(
        f'{NAME_APP}/world_skills_page.html',
        title='WorldSkills', contest=contest,
        past_contest=past_contest,
    )


@app.route('/contests-list')
def contests_list():
    contests = WorldSkillsContest.query.all()
    return render_template(f'{NAME_APP}/contests_list.html', title='WorldSkills contests', items=contests)


@app.route('/past-contests-list')
def past_contests_list():
    contests = WorldSkillsContest.query.all()
    past_contests = []
    for i in contests:
        if i.date < datetime.now().date():
            past_contests.append(i)

    return render_template(f'{NAME_APP}/contests_list.html', title='Past WorldSkills contests', items=past_contests)


@app.route('/contest/item=<id>')
def contests_instance(id):
    contest = WorldSkillsContest.query.filter_by(id=id)
    return render_template(f'{NAME_APP}/contests_instance.html', title='Contests', item=contest)
