from flask import Blueprint, render_template

NAME_APP = 'general'
app = Blueprint(NAME_APP, __name__)

@app.route('/')
def home_page():
    return render_template(f'{NAME_APP}/home.html', title='Home')

@app.route('/news')
def news():
    return render_template(f'{NAME_APP}/news.html', title='News')

@app.route('/news/item=<id>')
def news_item(id):
    return render_template(f'{NAME_APP}/news_item.html', title='News')