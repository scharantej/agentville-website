 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the routes for the application
@app.route('/')
def index():
    # Render the home page
    return render_template('index.html')

@app.route('/articles')
def articles():
    # Get all the articles from the database
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

    # Render the articles page with the list of articles
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    # Get the article with the specified ID from the database
    article = {
        'title': 'Article 1',
        'content': 'This is the content of article 1.'
    }

    # Render the article page with the article
    return render_template('article.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle the login request
    if request.method == 'POST':
        # Get the username and password from the request
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'admin' and password == 'secret':
            # Redirect to the home page if the login is successful
            return redirect(url_for('index'))
        else:
            # Render the login page again if the login is unsuccessful
            return render_template('login.html')
    else:
        # Render the login page if the request is a GET request
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Handle the signup request
    if request.method == 'POST':
        # Get the username and password from the request
        username = request.form['username']
        password = request.form['password']

        # Save the new user to the database

        # Redirect to the home page if the signup is successful
        return redirect(url_for('index'))
    else:
        # Render the signup page if the request is a GET request
        return render_template('signup.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
