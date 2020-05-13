from app import db

from flask_security import UserMixin, RoleMixin

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(70))
    last_name = db.Column(db.String(70))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    case = db.relationship('Case', back_populates='executor')

    posts = db.relationship('Posts', back_populates='author')

    def __repr__(self):
        return f'<{__class__.__name__} id: {self.id}, title: {self.email}>'


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
    # users = db.relationship('User', secondary=roles_users, backref=db.backref('roles', lazy='dynamic'))

    def __repr__(self):
        return f'<{__class__.__name__} id: {self.id}, title: {self.name}>'
