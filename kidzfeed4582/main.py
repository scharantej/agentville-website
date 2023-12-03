 
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'secret-key'

# Define the database
articles = []
users = {}

# Define the routes
@app.route('/')
def index():
    # Check if the user is logged in
    if 'username' in session:
        # Get the list of articles
        articles = get_articles()

        # Render the index page
        return render_template('index.html', articles=articles)
    else:
        # Redirect to the login page
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in
    if 'username' in session:
        # Redirect to the index page
        return redirect(url_for('index'))

    # Handle the login request
    if request.method == 'POST':
        # Get the username and password
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        if username in users and users[username]['password'] == password:
            # Log the user in
            session['username'] = username

            # Redirect to the index page
            return redirect(url_for('index'))
        else:
            # Display an error message
            return render_template('login.html', error='Invalid username or password')

    # Render the login page
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Check if the user is logged in
    if 'username' in session:
        # Log the user out
        session.pop('username')

    # Redirect to the login page
    return redirect(url_for('login'))

@app.route('/profile/<username>')
def profile(username):
    # Check if the user is logged in
    if 'username' in session:
        # Get the user's profile
        user = users[username]

        # Render the profile page
        return render_template('profile.html', user=user)
    else:
        # Redirect to the login page
        return redirect(url_for('login'))

@app.route('/article/<id>')
def article(id):
    # Check if the user is logged in
    if 'username' in session:
        # Get the article
        article = get_article(id)

        # Render the article page
        return render_template('article.html', article=article)
    else:
        # Redirect to the login page
        return redirect(url_for('login'))

@app.route('/post', methods=['GET', 'POST'])
def post():
    # Check if the user is logged in
    if 'username' in session:
        # Handle the post request
        if request.method == 'POST':
            # Get the article title and content
            title = request.form['title']
            content = request.form['content']

            # Create a new article
            article = {
                'id': len(articles) + 1,
                'title': title,
                'content': content,
                'author': session['username']
            }

            # Add the article to the database
            articles.append(article)

            # Redirect to the index page
            return redirect(url_for('index'))

        # Render the post page
        return render_template('post.html')
    else:
        # Redirect to the login page
        return redirect(url_for('login'))

# Define the API routes
@app.route('/api/login', methods=['POST'])
def api_login():
    # Get the username and password
    username = request.json['username']
    password = request.json['password']

    # Check if the user exists
    if username in users and users[username]['password'] == password:
        # Log the user in
        session['username'] = username

        # Return a success message
        return jsonify({'status': 'success'})
    else:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'Invalid username or password'})

@app.route('/api/logout')
def api_logout():
    # Check if the user is logged in
    if 'username' in session:
        # Log the user out
        session.pop('username')

        # Return a success message
        return jsonify({'status': 'success'})
    else:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'User not logged in'})

@app.route('/api/create_account', methods=['POST'])
def api_create_account():
    # Get the username and password
    username = request.json['username']
    password = request.json['password']

    # Check if the username is already taken
    if username in users:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'Username already taken'})

    # Create a new user
    users[username] = {
        'password': password,
        'followers': [],
        'following': []
    }

    # Return a success message
    return jsonify({'status': 'success'})

@app.route('/api/follow', methods=['POST'])
def api_follow():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the user to follow
        username = request.json['username']

        # Check if the user exists
        if username in users:
            # Add the user to the list of followers
            users[session['username']]['following'].append(username)

            # Add the user to the list of following
            users[username]['followers'].append(session['username'])

            # Return a success message
            return jsonify({'status': 'success'})
        else:
            # Return an error message
            return jsonify({'status': 'error', 'message': 'User not found'})
    else:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'User not logged in'})

@app.route('/api/unfollow', methods=['POST'])
def api_unfollow():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the user to unfollow
        username = request.json['username']

        # Check if the user exists
        if username in users:
            # Remove the user from the list of followers
            users[session['username']]['following'].remove(username)

            # Remove the user from the list of following
            users[username]['followers'].remove(session['username'])

            # Return a success message
            return jsonify({'status': 'success'})
        else:
            # Return an error message
            return jsonify({'status': 'error', 'message': 'User not found'})
    else:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'User not logged in'})

@app.route('/api/post_article', methods=['POST'])
def api_post_article():
    # Check if the user is logged in
    if 'username' in session:
        # Get the article title and content
        title = request.json['title']
        content = request.json['content']

        # Create a new article
        article = {
            'id': len(articles) + 1,
            'title': title,
            'content': content,
            'author': session['username']
        }

        # Add the article to the database
        articles.append(article)

        # Return a success message
        return jsonify({'status': 'success'})
    else:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'User not logged in'})

@app.route('/api/get_articles')
def api_get_articles():
    # Get the list of articles
    articles = get_articles()

    # Return the list of articles
    return jsonify({'articles': articles})

# Define the helper functions
def get_articles():
    # Return the list of articles
    return articles

def get_article(id):
    # Find the article with the specified ID
    for article in articles:
        if article['id'] == id:
            return article

    # Return None if the article was not found
    return None

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
