from app import db
from datetime import datetime


class WorldSkillsContest(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    images = db.Column(db.String(255), default='img/recipe__image.png')

    date = db.Column(db.Date(), default=datetime.now())

    def __repr__(self):
        return f'<{__class__.__name__} id: {self.id}, title: {self.title}>'



