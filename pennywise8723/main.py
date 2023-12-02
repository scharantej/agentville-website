 
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get('category')
        date = request.form.get('date')

        # Save the expense to the database.

        return redirect(url_for('view_expenses'))
    else:
        return render_template('add_expense.html')

@app.route('/view_expenses')
def view_expenses():
    # Get all expenses from the database.

    expenses = [
        {
            'amount': 100,
            'category': 'Food',
            'date': '2023-03-08'
        },
        {
            'amount': 200,
            'category': 'Transportation',
            'date': '2023-03-09'
        },
        {
            'amount': 300,
            'category': 'Entertainment',
            'date': '2023-03-10'
        }
    ]

    return render_template('view_expenses.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
