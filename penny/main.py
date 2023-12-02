 
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create the expenses table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date TEXT
)""")

# Create the categories table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)""")

# Define the routes
@app.route('/')
def index():
    # Get all the expenses
    expenses = c.execute('SELECT * FROM expenses').fetchall()

    # Get all the categories
    categories = c.execute('SELECT * FROM categories').fetchall()

    return render_template('index.html', expenses=expenses, categories=categories)

@app.route('/categories')
def categories():
    # Get all the categories
    categories = c.execute('SELECT * FROM categories').fetchall()

    return render_template('categories.html', categories=categories)

@app.route('/history')
def history():
    # Get all the expenses
    expenses = c.execute('SELECT * FROM expenses').fetchall()

    return render_template('history.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    # Get the form data
    category = request.form.get('category')
    amount = request.form.get('amount')
    date = request.form.get('date')

    # Insert the expense into the database
    c.execute('INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)',
              (category, amount, date))
    conn.commit()

    # Redirect to the home page
    return redirect(url_for('index'))

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    # Delete the expense from the database
    c.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()

    # Redirect to the home page
    return redirect(url_for('index'))

@app.route('/edit_expense/<int:id>', methods=['POST'])
def edit_expense(id):
    # Get the form data
    category = request.form.get('category')
    amount = request.form.get('amount')
    date = request.form.get('date')

    # Update the expense in the database
    c.execute('UPDATE expenses SET category = ?, amount = ?, date = ? WHERE id = ?',
              (category, amount, date, id))
    conn.commit()

    # Redirect to the home page
    return redirect(url_for('index'))

@app.route('/get_expenses')
def get_expenses():
    # Get all the expenses
    expenses = c.execute('SELECT * FROM expenses').fetchall()

    # Return the expenses in JSON format
    return jsonify(expenses)

@app.route('/get_categories')
def get_categories():
    # Get all the categories
    categories = c.execute('SELECT * FROM categories').fetchall()

    # Return the categories in JSON format
    return jsonify(categories)

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
