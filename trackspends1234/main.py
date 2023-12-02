 
from flask import Flask, render_template, request, jsonify
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
    categories = Category.query.all()
    return render_template('index.html', expenses=expenses, categories=categories)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = request.form.get('amount')
    category = request.form.get('category')
    date = request.form.get('date')

    expense = Expense(amount=amount, category=category, date=date)
    db.session.add(expense)
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

@app.route('/add_category', methods=['POST'])
def add_category():
    name = request.form.get('name')

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete_category/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/get_report')
def get_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    expenses = Expense.query.filter(Expense.date >= start_date, Expense.date <= end_date).all()
    report = {}
    for expense in expenses:
        if expense.category not in report:
            report[expense.category] = 0
        report[expense.category] += expense.amount

    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
