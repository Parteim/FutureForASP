from app import db


# ws_image = db.Table(
#     'ws_image',
#     db.Column('image_id', db.Integer(), db.ForeignKey('images.id')),
#     db.Column('ws_id', db.Integer(), db.ForeignKey('worldskills.id')),
# )


class WorldSkillsContest(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    # images = db.relationship('Images', secondary=ws_image, backref=db.backref('ws_contest', lazy='dynamic'))

    def __repr__(self):
        return f'<{__class__.__name__} id: {self.id}, title: {self.title}>'
