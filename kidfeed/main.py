 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get(article_id)
    return render_template('article.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
