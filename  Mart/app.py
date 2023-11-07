 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Product %r>' % self.name

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = request.cookies.get('cart')
    if cart:
        cart = cart.split(',')
        if product.id not in cart:
            cart.append(str(product.id))
        response = redirect(url_for('cart'))
        response.set_cookie('cart', ','.join(cart))
        return response
    else:
        response = redirect(url_for('cart'))
        response.set_cookie('cart', str(product.id))
        return response

@app.route('/cart')
def cart():
    cart = request.cookies.get('cart')
    if cart:
        cart = cart.split(',')
        products = Product.query.filter(Product.id.in_(cart))
        return render_template('cart.html', products=products)
    else:
        return render_template('cart.html', products=[])

@app.route('/checkout')
def checkout():
    cart = request.cookies.get('cart')
    if cart:
        cart = cart.split(',')
        products = Product.query.filter(Product.id.in_(cart))
        total_price = 0
        for product in products:
            total_price += product.price
        return render_template('checkout.html', products=products, total_price=total_price)
    else:
        return redirect(url_for('index'))

@app.route('/confirmation', methods=['POST'])
def confirmation():
    cart = request.cookies.get('cart')
    if cart:
        cart = cart.split(',')
        products = Product.query.filter(Product.id.in_(cart))
        for product in products:
            product.stock -= 1
            db.session.add(product)
        db.session.commit()
        response = redirect(url_for('index'))
        response.set_cookie('cart', '', expires=0)
        return response
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
