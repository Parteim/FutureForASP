### library  ==========
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import SQLAlchemyUserDatastore, Security
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

### local   ===========
from config import Configuration

#== models ==

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from user import models
from cases import models as cases_models
from conferences import models as conferences_models
from contests import models as contests_models
from general import models as general_models
from world_skills import models as world_skills_models

admin = Admin(app)
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(cases_models.Case, db.session))
admin.add_view(ModelView(conferences_models.Conference, db.session))
admin.add_view(ModelView(contests_models.Contest, db.session))
admin.add_view(ModelView(general_models.Images, db.session))
admin.add_view(ModelView(world_skills_models.WorldSkillsContest, db.session))

user_data_store = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_data_store)


