from app import db

from datetime import datetime


class Photos(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(255))

    date = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return f'<id:{self.id}; url:{self.url}>'