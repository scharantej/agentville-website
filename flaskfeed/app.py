 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'title': 'The First Article',
        'content': 'This is the first article.'
    },
    {
        'id': 2,
        'title': 'The Second Article',
        'content': 'This is the second article.'
    },
    {
        'id': 3,
        'title': 'The Third Article',
        'content': 'This is the third article.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((article for article in articles if article['id'] == article_id), None)
    if article is None:
        return redirect(url_for('index'))
    return render_template('article.html', article=article)

@app.route('/reading_list')
def reading_list():
    return render_template('reading_list.html', articles=articles)

@app.route('/share/<int:article_id>')
def share(article_id):
    article = next((article for article in articles if article['id'] == article_id), None)
    if article is None:
        return redirect(url_for('index'))
    return render_template('share.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)
