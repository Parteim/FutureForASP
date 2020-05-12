from app import db
from datetime import datetime


class Case(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    customer = db.Column(db.String(255))
    date = db.Column(db.Date(), default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor = db.relationship('User', back_populates='case')

    def __repr__(self):
        return f'<Case id: {self.id}, title: {self.title}>'
