 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'Article 1',
            'content': 'This is the content of article 1.'
        },
        {
            'title': 'Article 2',
            'content': 'This is the content of article 2.'
        },
        {
            'title': 'Article 3',
            'content': 'This is the content of article 3.'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = {
        'title': 'Article {}'.format(article_id),
        'content': 'This is the content of article {}.'.format(article_id)
    }
    return render_template('article.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials.')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO: Save the user to the database.
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
