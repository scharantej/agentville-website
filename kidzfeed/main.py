 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  articles = Article.query.all()
  return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
  article = Article.query.get(article_id)
  return render_template('article.html', article=article)

if __name__ == '__main__':
  app.run()
