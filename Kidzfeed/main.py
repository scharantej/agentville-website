 
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.newsfeed_for_kids

@app.route('/')
def index():
  articles = db.articles.find()
  return render_template('index.html', articles=articles)

@app.route('/article/<id>')
def article(id):
  article = db.articles.find_one({'_id': ObjectId(id)})
  return render_template('article.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = db.users.find_one({'username': username, 'password': password})
    if user:
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
    user = db.users.insert_one({'username': username, 'password': password})
    if user:
      return redirect(url_for('index'))
    else:
      return render_template('signup.html', error='Error creating user')
  else:
    return render_template('signup.html')

if __name__ == '__main__':
  app.run(debug=True)
