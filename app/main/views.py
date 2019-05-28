from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_article



@main.route('/')
def index():
    """
    Function that returns the index page and all its data
    """
    general_news = get_sources('general')
    return render_template('index.html', general_news=general_news)

#
@main.route('/source/<id>')
def articles(id):
    """
    View articles
    """
    article = get_article(id)
    print(article)
    return render_template('news.html', article=article, id=id)