from flask import Blueprint, render_template

NAME_APP = 'world_skills'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def world_skills_page():
    return render_template(f'{NAME_APP}/world_skills_page.html', title='WorldSkills')
