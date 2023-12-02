 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsfeed.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.title

@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

@app.route('/saved_articles')
def saved_articles():
    articles = Article.query.filter_by(saved=True).all()
    return render_template('saved_articles.html', articles=articles)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/save_article/<int:id>')
def save_article(id):
    article = Article.query.get(id)
    article.saved = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/unsave_article/<int:id>')
def unsave_article(id):
    article = Article.query.get(id)
    article.saved = False
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
