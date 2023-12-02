 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boats.db'
db = SQLAlchemy(app)

class Boat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  price = db.Column(db.Float, nullable=False)
  image_url = db.Column(db.String(255), nullable=False)
  contact_info = db.Column(db.String(255), nullable=False)

  def __repr__(self):
    return '<Boat %r>' % self.name

@app.route("/")
def index():
  boats = Boat.query.all()
  return render_template("index.html", boats=boats)

@app.route("/boat/<int:boat_id>")
def boat(boat_id):
  boat = Boat.query.get(boat_id)
  return render_template("boat.html", boat=boat)

@app.route("/contact/<int:boat_id>", methods=["POST"])
def contact(boat_id):
  boat = Boat.query.get(boat_id)
  name = request.form["name"]
  email = request.form["email"]
  message = request.form["message"]
  send_email(boat.seller_email, name, email, message)
  return render_template("contact.html", boat=boat)

if __name__ == "__main__":
  app.run()
