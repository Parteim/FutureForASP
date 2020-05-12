from app import db
from datetime import datetime

contest_image = db.Table(
    'contest_image',
    db.Column('contest_id', db.Integer(), db.ForeignKey('contest.id')),
    db.Column('image_id', db.Integer(), db.ForeignKey('images.id')),
)


class Contest(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    images = db.relationship('Images', secondary=contest_image, backref=db.backref('contest', lazy='dynamic'))

    start = db.Column(db.Date())
    end = db.Column(db.Date())

    def __repr__(self):
        return f'<{__class__.__name__} id: {self.id}, title: {self.title}>'
