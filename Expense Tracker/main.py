
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  expenses = Expense.query.all()
  return render_template('index.html', expenses=expenses)

@app.route('/expense/<id>')
def expense(id):
  expense = Expense.query.get(id)
  return render_template('expense.html', expense=expense)

@app.route('/category')
def category():
  categories = Category.query.all()
  return render_template('category.html', categories=categories)

@app.route('/search')
def search():
  q = request.args.get('q')
  expenses = Expense.query.filter(Expense.title.contains(q))
  return render_template('search.html', expenses=expenses)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  else:
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
      return redirect(url_for('index'))
    else:
      return render_template('login.html', error='Invalid credentials')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  else:
    username = request.form['username']
    password = request.form['password']
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run()
