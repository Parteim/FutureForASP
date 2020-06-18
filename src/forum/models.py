from app import db

from datetime import datetime


class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='posts')

    title = db.Column(db.String(150))
    text = db.Column(db.Text())
    files = db.relationship('PostsFiles', back_populates='post')
    date = db.Column(db.DateTime(), default=datetime.now())

    comment = db.relationship('Comments', back_populates='post')

    def __repr__(self):
        return f'<id:{self.id}; title:{self.title}>'


class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='comment')

    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))
    post = db.relationship('Posts', back_populates='comment')

    text = db.Column(db.Text())


class PostsFiles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(255))

    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))
    post = db.relationship('Posts', back_populates='files')