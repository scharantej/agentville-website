 
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

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)

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

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)

    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/create_category', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        name = request.form['name']

        category = Category(name=name)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('create_category.html')

@app.route('/edit_category/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)

    if request.method == 'POST':
        name = request.form['name']

        category.name = name

        db.session.commit()

        return redirect(url_for('categories'))

    return render_template('edit_category.html', category=category)

@app.route('/delete_category/<int:id>')
def delete_category(id):
    category = Category.query.get_or_404(id)

    db.session.delete(category)
    db.session.commit()

    return redirect(url_for('categories'))

@app.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        category = request.form['category']

        expenses = Expense.query.filter(Expense.date >= start_date, Expense.date <= end_date)

        if category != 'All':
            expenses = expenses.filter(Expense.category == category)

        total_amount = expenses.sum(Expense.amount)

        return render_template('report.html', expenses=expenses, total_amount=total_amount)

    return render_template('generate_report.html')

if __name__ == '__main__':
    app.run(debug=True)
