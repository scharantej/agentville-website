 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boats.db'
db = SQLAlchemy(app)

class Boat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Boat %r>' % self.name

@app.route('/')
def index():
    boats = Boat.query.all()
    return render_template('index.html', boats=boats)

@app.route('/boats')
def boats():
    boats = Boat.query.all()
    return render_template('boats.html', boats=boats)

@app.route('/boats/<int:boat_id>')
def boat_detail(boat_id):
    boat = Boat.query.get(boat_id)
    return render_template('boat_detail.html', boat=boat)

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send the email
        return render_template('contact_us.html', message_sent=True)
    else:
        return render_template('contact_us.html', message_sent=False)

if __name__ == '__main__':
    app.run()
