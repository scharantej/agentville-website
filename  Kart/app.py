 
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

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        product = Product(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_product.html', product=product)

@app.route('/delete/<int:id>')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


html
<!DOCTYPE html>
<html>
<head>
  <title>Products</title>
</head>
<body>
  <h1>Products</h1>
  <ul>
    {% for product in products %}
      <li>{{ product.name }} - {{ product.price }}</li>
    {% endfor %}
  </ul>
  <a href="{{ url_for('add_product') }}">Add Product</a>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
  <title>Add Product</title>
</head>
<body>
  <h1>Add Product</h1>
  <form action="{{ url_for('add_product') }}" method="POST">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="price">Price:</label><br>
    <input type="number" id="price" name="price"><br><br>
    <input type="submit" value="Add">
  </form>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
  <title>Edit Product</title>
</head>
<body>
  <h1>Edit Product</h1>
  <form action="{{ url_for('edit_product', id=product.id) }}" method="POST">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" value="{{ product.name }}"><br>
    <label for="price">Price:</label><br>
    <input type="number" id="price" name="price" value="{{ product.price }}"><br><br>
    <input type="submit" value="Edit">
  </form>
</body>
</html>
