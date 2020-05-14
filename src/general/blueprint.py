from flask import Blueprint, render_template
from sqlalchemy import desc

from .models import Recipes, News, Ads

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
    return render_template(f'{NAME_APP}/instance.html', title='News')


@app.route('/recipes')
def recipes():
    recipes_list = Recipes.query.order_by(desc(Recipes.date))
    return render_template(f'{NAME_APP}/recipes.html', title='Recipe', recipes=recipes_list)


@app.route('/recipes/item=<id>')
def recipes_item(id):
    recipe = Recipes.query.filter_by(id=id).first()
    return render_template(f'{NAME_APP}/instance.html', title='Recipe', item=recipe)
