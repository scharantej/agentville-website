 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  price = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return '<Product %r>' % self.name

class CartItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
  product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))
  quantity = db.Column(db.Integer, nullable=False)

  def __repr__(self):
    return '<CartItem %r>' % self.product.name

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/products')
def products():
  products = Product.query.all()
  return render_template('products.html', products=products)

@app.route('/cart')
def cart():
  cart_items = CartItem.query.all()
  return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
  product_id = request.form.get('product_id')
  product = Product.query.get(product_id)
  cart_item = CartItem(product=product, quantity=1)
  db.session.add(cart_item)
  db.session.commit()
  return redirect(url_for('cart'))

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
  cart_item_id = request.form.get('cart_item_id')
  cart_item = CartItem.query.get(cart_item_id)
  db.session.delete(cart_item)
  db.session.commit()
  return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
  cart_items = CartItem.query.all()
  total_price = 0
  for cart_item in cart_items:
    total_price += cart_item.product.price * cart_item.quantity
  return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

if __name__ == '__main__':
  app.run(debug=True)
