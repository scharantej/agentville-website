 
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

    def __repr__(self):
        return '<Expense %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']

        expense = Expense(name=name, amount=amount, category=category)
        db.session.add(expense)
        db.session.commit()

        return redirect(url_for('view_expenses'))

    return render_template('add_expense.html')

@app.route('/view_expenses')
def view_expenses():
    expenses = Expense.query.all()
    return render_template('view_expenses.html', expenses=expenses)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
