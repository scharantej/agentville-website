 
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('expenses', lazy=True))

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
    name = request.form['name']
    amount = float(request.form['amount'])
    category_id = int(request.form['category_id'])
    expense = Expense(name=name, amount=amount, category_id=category_id)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.name = request.form['name']
        expense.amount = float(request.form['amount'])
        expense.category_id = int(request.form['category_id'])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_expense.html', expense=expense)

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
    db.create_all()
    app.run(debug=True)
