 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boats.db'
db = SQLAlchemy(app)

class Boat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  image_url = db.Column(db.String(255), nullable=False)
  price = db.Column(db.Float, nullable=False)
  contact_info = db.Column(db.String(255), nullable=False)

  def __repr__(self):
    return '<Boat %r>' % self.name

@app.route("/")
def index():
  boats = Boat.query.all()
  return render_template("index.html", boats=boats)

@app.route("/boats/<int:boat_id>")
def boat_detail(boat_id):
  boat = Boat.query.get(boat_id)
  return render_template("boat_detail.html", boat=boat)

@app.route("/contact_us")
def contact_us():
  return render_template("contact_us.html")

if __name__ == "__main__":
  db.create_all()
  app.run(debug=True)
