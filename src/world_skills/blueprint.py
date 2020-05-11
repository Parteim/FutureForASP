from flask import Blueprint, render_template

NAME_APP = 'world_skills'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def world_skills_page():
    return render_template(f'{NAME_APP}/world_skills_page.html', title='WorldSkills')

@app.route('/contests-list')
def contests_list():
    return render_template(f'{NAME_APP}/contests_list.html', title='Contests')

@app.route('/past-contests-list')
def past_contests_list():
    return render_template(f'{NAME_APP}/contests_list.html', title='Past contests')

@app.route('/contest/item=<id>')
def contests_instance(id):
    return render_template(f'{NAME_APP}/contests_instance.html', title='Contests')