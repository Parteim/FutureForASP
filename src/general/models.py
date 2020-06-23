from app import db

from datetime import datetime

news_images = db.Table(
    'news_images',
    db.Column('image_id', db.Integer(), db.ForeignKey('images.id')),
    db.Column('news_id', db.Integer(), db.ForeignKey('news.id')),
)


class Images(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(255))

    date = db.Column(db.DateTime(), default=datetime.now())


class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    date = db.Column(db.Date(), default=datetime.now())

    images = db.relationship('Images', secondary=news_images, backref=db.backref('news', lazy='dynamic'))


class Recipes(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    date = db.Column(db.Date(), default=datetime.now())

    images = db.Column(db.String(255), default='img/recipe__image.png')


class Ads(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    text = db.Column(db.Text())
    date = db.Column(db.Date(), default=datetime.now())
