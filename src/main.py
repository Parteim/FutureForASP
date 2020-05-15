from app import app, db

#== app register ==
from general.blueprint import app as main_app
from contests.blueprint import app as contest_app
from conferences.blueprint import app as conferences_app
from world_skills.blueprint import app as world_skills_app
from cases.blueprint import app as cases_app
from forum.blueprint import app as forum_app
from gallery.blueprint import app as gallery_app
from user.blueprint import app as user_app


app.register_blueprint(main_app, url_prefix='/')
app.register_blueprint(contest_app, url_prefix='/contests')
app.register_blueprint(conferences_app, url_prefix='/conferences')
app.register_blueprint(world_skills_app, url_prefix='/world_skills')
app.register_blueprint(cases_app, url_prefix='/cases')
app.register_blueprint(forum_app, url_prefix='/forum')
app.register_blueprint(gallery_app, url_prefix='/gallery')
app.register_blueprint(user_app, url_prefix='/user_app')

if __name__ == '__main__':
    app.run()