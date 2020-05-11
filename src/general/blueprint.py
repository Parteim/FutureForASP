from flask import Blueprint, render_template

NAME_APP = 'general'
app = Blueprint(NAME_APP, __name__)

@app.route('/')
def home_page():
    return render_template(f'{NAME_APP}/home.html', title='Home')

@app.route('/news')
def news():
    return render_template(f'{NAME_APP}/items_list.html', title='News')

@app.route('/news/item=<id>')
def news_item(id):
    return render_template(f'{NAME_APP}/instance.html', title='News')

@app.route('/recipes')
def recipes():
    return render_template(f'{NAME_APP}/recipes.html', title='Recipe')

@app.route('/recipes/item=<id>')
def recipes_item(id):
    return render_template(f'{NAME_APP}/instance.html', title='Recipe')