from flask import render_template
from app import app
from app.request import get_articles, get_news

@app.route('/')
def index():
    general_news = get_news('general')
    health_news = get_news('health')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    entertainment_news = get_news('entertainment')
    title = 'News Web'
    return render_template('index.html',title = title,general=general_news, health=health_news, sports=sports_news, technology=technology_news,entertainment=entertainment_news)

@app.route('/articles')
def articles():
    all_sources = get_articles('general')
    title = 'News Web'
    return render_template('articles.html',general=all_sources,title=title)