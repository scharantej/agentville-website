 
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = 'secret-key'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Product %r>' % self.name

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))
    user = db.relationship('User', backref=db.backref('cart_items', lazy=True))

    def __repr__(self):
        return '<CartItem %r>' % self.id

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if request.method == 'POST':
        quantity = request.form.get('quantity')
        if quantity and quantity.isdigit():
            quantity = int(quantity)
            product = Product.query.get_or_404(product_id)
            cart_item = CartItem(product_id=product.id, quantity=quantity, user_id=current_user.id)
            db.session.add(cart_item)
            db.session.commit()
            flash('Product added to cart successfully!', 'success')
        else:
            flash('Invalid quantity!', 'danger')
    return redirect(url_for('index'))

@app.route('/shopping_cart')
def shopping_cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.product.price * cart_item.quantity
    return render_template('shopping_cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/checkout', methods=['POST'])
def checkout():
    if request.method == 'POST':
        payment_method = request.form.get('payment_method')
        if payment_method == 'credit_card':
            # Process credit card payment
            # ...
            flash('Payment successful!', 'success')
            return redirect(url_for('confirmation'))
        else:
            flash('Invalid payment method!', 'danger')
            return redirect(url_for('shopping_cart'))
    return render_template('checkout.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
