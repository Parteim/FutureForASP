from app import db

from datetime import datetime


class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='posts')

    title = db.Column(db.String(150))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.now())

    comment = db.relationship('Comments', back_populates='post')


class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='comment')

    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))
    post = db.relationship('Posts', back_populates='comment')

    text = db.Column(db.Text())
