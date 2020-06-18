from flask import Blueprint, render_template
from sqlalchemy import desc

from .models import Photos

NAME_APP = 'gallery'

app = Blueprint(NAME_APP, __name__)


@app.route('/')
def gallery_page():
    items = Photos.query.order_by(desc(Photos.date)).all()
    return render_template(f'{NAME_APP}/gallery_page.html', title='Gallery', items=items)