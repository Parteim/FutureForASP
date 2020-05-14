from flask import Blueprint, render_template
from sqlalchemy import desc
from datetime import datetime

from .models import Conference

NAME_APP = 'conferences'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def conferences_page():
    upcoming_conference = None
    past_conference = None
    for i in Conference.query.all():
        if i.date < datetime.now().date():
            past_conference = i
        elif i.date > datetime.now().date():
            upcoming_conference = i
    return render_template(
        f'{NAME_APP}/conferences.html',
        title='Conferences',
        u_conf=upcoming_conference,
        p_conf=past_conference,
    )


@app.route('/conferences-list')
def conferences_list():
    items = Conference.query.order_by(desc(Conference.date))
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Conferences', items=items)


@app.route('/past-conferences-list')
def past_conferences_list():
    contests = Conference.query.all()
    past_conferences = []
    for i in contests:
        if i.date < datetime.now().date():
            past_conferences.append(i)

    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Past conferences', items=past_conferences)


@app.route('/conferences/item=<id>')
def conferences_instance(id):
    item = Conference.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Conferences', item=item)
