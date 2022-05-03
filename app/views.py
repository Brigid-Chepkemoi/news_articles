from flask import render_template
from app import app
from app.request import get_articles, get_articles_headlines, get_news

@app.route('/')
def index():
    general_news = get_news('general')
    health_news = get_news('health')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    entertainment_news = get_news('entertainment')
    articles_news = get_articles("general")
    title = 'News Web'
    abc_news = get_articles_headlines('abc-news')
    cnn_news = get_articles_headlines('cnn')
    aljazeera = get_articles_headlines('al-jazeera-english')
    return render_template('index.html',title = title,general=general_news, health=health_news, sports=sports_news, technology=technology_news,entertainment=entertainment_news,articles=articles_news,abc=abc_news,cnn=cnn_news,aljazeera=aljazeera)

@app.route('/articles')
def articles():
    articles = get_articles('general')
    title = 'News Web'
    return render_template('articles.html',articles=articles,title=title)