 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
db = SQLAlchemy(app)

class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return '<Article %r>' % self.title

@app.route('/')
def index():
  articles = Article.query.all()
  return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
  article = Article.query.get(article_id)
  return render_template('article.html', article=article)

@app.route('/share/<int:article_id>', methods=['POST'])
def share(article_id):
  email = request.form['email']
  article = Article.query.get(article_id)
  send_email(email, article)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
