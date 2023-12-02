 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/article/<int:id>')
def article(id):
  return render_template('article.html', id=id)

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
    # TODO: Save the user to the database
    return redirect(url_for('index'))
  else:
    return render_template('signup.html')

if __name__ == '__main__':
  app.run(debug=True)
