 
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    amount = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('expenses', lazy=True))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    name = request.form['name']
    amount = float(request.form['amount'])
    category_id = int(request.form['category_id'])
    expense = Expense(name=name, amount=amount, category_id=category_id)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expense.query.get(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_expense/<int:id>', methods=['POST'])
def edit_expense(id):
    expense = Expense.query.get(id)
    expense.name = request.form['name']
    expense.amount = float(request.form['amount'])
    expense.category_id = int(request.form['category_id'])
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/get_expenses')
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses])

@app.route('/get_categories')
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

if __name__ == '__main__':
    app.run(debug=True)
