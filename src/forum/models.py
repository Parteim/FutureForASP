from app import db

from datetime import datetime


class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    user_id = db.Column(db.Integer, db.ForeigneKey('user.id'))
    author = db.relationship('User', back_populates='posts')

    title = db.Column(db.String(200))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), defaul=datetime.now())