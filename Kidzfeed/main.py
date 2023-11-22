 
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

@app.route('/index')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('signup.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        author = request.form['author']
        date = datetime.datetime.now()
        new_article = Article(title=title, body=body, author=author, date=date)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('submit.html')

@app.route('/admin')
def admin():
    articles = Article.query.all()
    return render_template('admin.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
