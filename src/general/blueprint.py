from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import desc

import config

import os

from .models import Recipes, News, Ads, db
from app import user_data_store

NAME_APP = 'general'
app = Blueprint(NAME_APP, __name__)


@app.route('/')
def home_page():
    recipe = Recipes.query.order_by(desc(Recipes.date)).first()
    news_list = News.query.order_by(desc(News.date))[:2]
    ads = Ads.query.order_by(desc(Ads.date)).first()
    return render_template(f'{NAME_APP}/home.html', title='Home', recipe=recipe, news_list=news_list, ads=ads)


@app.route('/news')
def news():
    news_list = News.query.order_by(desc(News.date)).all()
    return render_template(f'{NAME_APP}/items_list.html', title='News', items=news_list)


@app.route('/news/item=<id>')
def news_item(id):
    item = News.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/instance.html', title='News', item=item)


@app.route('/recipes')
def recipes():
    recipes_list = Recipes.query.order_by(desc(Recipes.date))
    return render_template(f'{NAME_APP}/recipes.html', title='Recipe', recipes=recipes_list)


@app.route('/recipes/item=<id>')
def recipes_item(id):
    recipe = Recipes.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/instance.html', title='Recipe', item=recipe)


@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'POST':
        print(request.files.getlist('file[]'))
        for f in request.files.getlist('file[]'):
            f.save(config.Configuration.UPLOAD_FOLDER + f.filename)

    return render_template(f'{NAME_APP}/upload_form.html', title='Upload')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        f_name = request.form['first_name']
        l_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        a_password = request.form['repeat_password']

        if password == a_password:
            user_data_store.create_user(
                first_name=f_name,
                last_name=l_name,
                email=email,
                password=password,
            )
            db.session.commit()

            return redirect(url_for("security.login"))
    return render_template('security/register.html', title='Регистрация')

