from flask import Blueprint, render_template

from datetime import datetime

from .models import Conference

NAME_APP = 'conferences'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def conferences_page():
    conferences = Conference.query.order_by('date')
    upcoming_conference = conferences.first()
    for i in conferences:
        if i.date < datetime.now().date():
            past_conference = i
    return render_template(
        f'{NAME_APP}/conferences.html',
        title='Conferences',
        u_conf=upcoming_conference,
        p_conf=past_conference,
    )


@app.route('/conferences-list')
def conferences_list():
    items = Conference.query.all()
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Conferences', items=items)


@app.route('/past-conferences-list')
def past_conferences_list():
    return render_template(f'{NAME_APP}/{NAME_APP}_list.html', title='Past conferences')


@app.route('/conferences/item=<id>')
def conferences_instance(id):
    item = Conference.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/{NAME_APP}_instance.html', title='Conferences', item=item)
