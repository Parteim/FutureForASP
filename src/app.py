### library  ==========
from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

### local   ===========
from config import Configuration

# == models ==

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
from forum import models as forum_models


class ForumView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/forum.html')


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


admin = Admin(app, 'FlaskApp', url='/admin', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(models.User, db.session, category='User'))
admin.add_view(AdminView(models.Role, db.session, category='User'))
admin.add_view(AdminView(cases_models.Case, db.session))
admin.add_view(AdminView(conferences_models.Conference, db.session))
admin.add_view(AdminView(contests_models.Contest, db.session))
admin.add_view(AdminView(general_models.Images, db.session, category='General'))
admin.add_view(AdminView(general_models.News, db.session, category='General'))
admin.add_view(AdminView(general_models.Recipes, db.session, category='General'))
admin.add_view(AdminView(general_models.Ads, db.session, category='General'))
admin.add_view(AdminView(world_skills_models.WorldSkillsContest, db.session))
admin.add_view(AdminView(forum_models.Posts, db.session, category="Forum"))
admin.add_view(AdminView(forum_models.Comments, db.session, category="Forum"))
# admin.add_view(ForumView(name='Forum', endpoint='analytics')

user_data_store = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_data_store)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('general/404.html'), 404
