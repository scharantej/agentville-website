 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    news_articles = get_news_articles()
    return render_template('index.html', news_articles=news_articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = get_article_by_id(article_id)
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run()
