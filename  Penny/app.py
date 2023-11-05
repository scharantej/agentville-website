 
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Expense %r>' % self.id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']

        expense = Expense(amount=amount, category=category, date=date)
        db.session.add(expense)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_expense.html')

@app.route('/edit_expense/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']

        expense.amount = amount
        expense.category = category
        expense.date = date

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit_expense.html', expense=expense)

@app.route('/delete_expense/<int:expense_id>')
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']

        category = Category(name=name)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('add_category.html')

@app.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)

    if request.method == 'POST':
        name = request.form['name']

        category.name = name

        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('edit_category.html', category=category)

@app.route('/delete_category/<int:category_id>')
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)

    db.session.delete(category)
    db.session.commit()

    return redirect(url_for('categories'))

if __name__ == '__main__':
    app.run(debug=True)
