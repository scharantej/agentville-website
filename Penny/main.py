 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  amount = db.Column(db.Float)
  category = db.Column(db.String(50))
  date = db.Column(db.DateTime)

  def __repr__(self):
    return '<Expense %r>' % self.name

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
  if request.method == 'GET':
    return render_template('add_expense.html')
  else:
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    expense = Expense(name=name, amount=amount, category=category)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_expense/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
  expense = Expense.query.get(expense_id)
  if request.method == 'GET':
    return render_template('edit_expense.html', expense=expense)
  else:
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    expense.name = name
    expense.amount = amount
    expense.category = category
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_expense/<int:expense_id>', methods=['GET', 'POST'])
def delete_expense(expense_id):
  expense = Expense.query.get(expense_id)
  if request.method == 'GET':
    return render_template('delete_expense.html', expense=expense)
  else:
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/view_expenses')
def view_expenses():
  expenses = Expense.query.all()
  return render_template('view_expenses.html', expenses=expenses)

if __name__ == '__main__':
  app.run(debug=True)
