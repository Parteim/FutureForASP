from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required, current_user
from sqlalchemy import desc
import os

import config

from .models import Posts, PostsFiles, db, Comments

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
    files = request.files.getlist('files[]')
    author = current_user

    if title == '' or len(text) < 50:
        return redirect(url_for('forum.forum_page'))

    try:
        post = Posts(title=title, text=text, author=author)
        db.session.add(post)
        db.session.commit()

    except Exception:
        print('Something wrong')
    for file in files:
        condition = True
        counter = 0
        while condition:
            filename = file.filename
            if filename not in os.listdir(config.Configuration.UPLOAD_FOLDER + f'{NAME_APP}\\'):
                file_path = config.Configuration.UPLOAD_FOLDER + f'{NAME_APP}/' + filename
                condition = False
            else:
                counter += 1
                file_path = config.Configuration.UPLOAD_FOLDER + f'{NAME_APP}/' + str(counter) + filename
                condition = False
        file.save(file_path)
        url = file_path.split('static')[1]
        print(url)
        file_post = PostsFiles(url=url, post_id=Posts.query.all()[-1].id)
        db.session.add(file_post)
        db.session.commit()
    return redirect(url_for('forum.forum_page'))


@app.route('/edit-post/<id>', methods=['POST'])
@login_required
def edit_post(id):
    title = request.form['title']
    text = request.form['text']
    try:
        query = db.session.query(Posts).filter(Posts.id == id). \
            update({Posts.title: title, Posts.text: text}, synchronize_session=False)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return redirect(url_for('forum.instance_post', id=id))
    return redirect(url_for('forum.instance_post', id=id))


@app.route('/instance-post/<id>')
def instance_post(id):
    post = Posts.query.filter_by(id=id).first()
    file_list = post.files
    return render_template(f'{NAME_APP}/instance_post.html', item=post, title=post.title, files=file_list)


@app.route('/search-post', methods=['POST'])
def search_post():
    condition = request.form['condition']
    posts = []
    posts.extend(Posts.query.filter(Posts.title.like(f'%{condition}%')))
    posts.extend(Posts.query.filter(Posts.text.like(f'%{condition}%')))
    return render_template(f'{NAME_APP}/forum_page.html', title='Forum', posts=posts)


@app.route('/create-comment/<id>', methods=['POST'])
def create_comment(id):
    comment = Comments(
        user_id=current_user.id,
        post_id=id,
        text=request.form['text'],
    )
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('forum.instance_post', id=id))