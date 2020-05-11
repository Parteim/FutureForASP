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

admin = Admin(app)
admin.add_view(ModelView(models.User, db.session))

user_data_store = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_data_store)


