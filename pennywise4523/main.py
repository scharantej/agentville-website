 
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Expense %r>' % self.id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expenses/')
def expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/expenses/add/', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        date = request.form['date']
        category = request.form['category']

        expense = Expense(amount=amount, date=date, category=category)
        db.session.add(expense)
        db.session.commit()

        return redirect(url_for('expenses'))

    return render_template('add_expense.html')

@app.route('/expenses/edit/<int:id>/', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        amount = request.form['amount']
        date = request.form['date']
        category = request.form['category']

        expense.amount = amount
        expense.date = date
        expense.category = category

        db.session.commit()

        return redirect(url_for('expenses'))

    return render_template('edit_expense.html', expense=expense)

@app.route('/expenses/delete/<int:id>/', methods=['GET', 'POST'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(expense)
        db.session.commit()

        return redirect(url_for('expenses'))

    return render_template('delete_expense.html', expense=expense)

@app.route('/categories/')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@app.route('/categories/add/', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']

        category = Category(name=name)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('add_category.html')

@app.route('/categories/edit/<int:id>/', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)

    if request.method == 'POST':
        name = request.form['name']

        category.name = name

        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('edit_category.html', category=category)

@app.route('/categories/delete/<int:id>/', methods=['GET', 'POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(category)
        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('delete_category.html', category=category)

@app.route('/reports/')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
