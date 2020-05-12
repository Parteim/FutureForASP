from app import db
from datetime import datetime

conference_image = db.Table(
    'conference_image',
    db.Column('conference_id', db.Integer(), db.ForeignKey('conference.id')),
    db.Column('image_id', db.Integer(), db.ForeignKey('images.id')),
)


class Conference(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    images = db.relationship('Images', secondary=conference_image, backref=db.backref('conference', lazy='dynamic'))

    date = db.Column(db.Date(), default=datetime)

    def __repr__(self):
        return f'<{__class__.__name__} id: {self.id}, title: {self.title}>'
