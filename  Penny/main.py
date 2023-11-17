 
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    category = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Expense %r>' % self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        new_expense = Expense(name=name, amount=amount, category=category)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    if request.method == 'GET':
        expense = Expense.query.get_or_404(id)
        return render_template('edit_expense.html', expense=expense)
    elif request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        expense = Expense.query.get_or_404(id)
        expense.name = name
        expense.amount = amount
        expense.category = category
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
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
