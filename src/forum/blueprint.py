from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required, current_user
from sqlalchemy import desc

from .models import Posts, db

NAME_APP = 'forum'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def forum_page():
    posts = Posts.query.order_by(desc(Posts.date))
    return render_template(f'{NAME_APP}/forum_page.html', title='Forum', posts=posts)


@app.route('/create-post/', methods=['POST'])
@login_required
def create_post():
    title = request.form['title']
    text = request.form['text']
    author = current_user

    try:
        post = Posts(title=title, text=text, author=author)
        db.session.add(post)
        db.session.commit()
    except Exception:
        print('Something wrong')
    return redirect(url_for('forum.forum_page'))


@app.route('/edit-post/<id>')
@login_required
def edit_post(id):
    pass


@app.route('/instance-post/<id>')
def instance_post(id):
    post = Posts.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/instance_post.html', item=post)


@app.route('/search-post', methods=['POST'])
def search_post():
    condition = request.form['condition']
    posts = []
    posts.extend(Posts.query.filter(Posts.title.like(f'%{condition}%')))
    posts.extend(Posts.query.filter(Posts.text.like(f'%{condition}%')))
    return render_template(f'{NAME_APP}/forum_page.html', title='Forum', posts=posts)
