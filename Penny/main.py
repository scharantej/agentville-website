 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Expense %r>' % self.name

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']

        expense = Expense(name=name, amount=amount, category=category, date=date)
        db.session.add(expense)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_expense.html')

@app.route('/edit_expense/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if request.method == 'POST':
        expense.name = request.form['name']
        expense.amount = request.form['amount']
        expense.category = request.form['category']
        expense.date = request.form['date']

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit_expense.html', expense=expense)

@app.route('/delete_expense/<int:expense_id>')
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/categories')
def categories():
    categories = Expense.query.distinct(Expense.category).all()
    return render_template('categories.html', categories=categories)

@app.route('/trends')
def trends():
    expenses = Expense.query.all()
    return render_template('trends.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
