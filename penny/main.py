 
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

    def __repr__(self):
        return '<Expense %r>' % self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Category %r>' % self.name

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@app.route('/history')
def history():
    expenses = Expense.query.all()
    return render_template('history.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    name = request.form['name']
    category = request.form['category']
    amount = float(request.form['amount'])
    date = request.form['date']

    expense = Expense(name=name, category=category, amount=amount, date=date)
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
    expense.category = request.form['category']
    expense.amount = float(request.form['amount'])
    expense.date = request.form['date']

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
