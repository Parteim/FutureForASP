### library  ==========
from flask import Flask

### local   ===========
from config import Configuration
#== app register ==
from general.blueprint import app as main_app
from contests.blueprint import app as contest_app
from conferences.blueprint import app as conferences_app
from world_skills.blueprint import app as world_skills_app
from cases.blueprint import app as cases_app
from forum.blueprint import app as forum_app
from gallery.blueprint import app as gallery_app

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(main_app, url_prefix='/')
app.register_blueprint(contest_app, url_prefix='/contest')
app.register_blueprint(conferences_app, url_prefix='/conferences')
app.register_blueprint(world_skills_app, url_prefix='/world_skills')
app.register_blueprint(cases_app, url_prefix='/cases')
app.register_blueprint(forum_app, url_prefix='/forum')
app.register_blueprint(gallery_app, url_prefix='/gallery')
