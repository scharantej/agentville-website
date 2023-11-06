 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores.db'
db = SQLAlchemy(app)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    die1 = db.Column(db.Integer)
    die2 = db.Column(db.Integer)
    total = db.Column(db.Integer)
    color = db.Column(db.String(10))

    def __repr__(self):
        return '<Score %r>' % self.id

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roll", methods=["POST"])
def roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    color = "green"
    if die1 == 1 and die2 == 1:
        color = "green"
    elif die1 == 6 and die2 == 6:
        color = "green"
    elif die1 == die2 and die1 != 1 and die1 != 6:
        color = "blue"
    else:
        color = "red"

    score = Score(die1=die1, die2=die2, total=total, color=color)
    db.session.add(score)
    db.session.commit()

    return render_template("index.html", result=score)

@app.route("/scores")
def scores():
    scores = Score.query.all()
    return render_template("scores.html", scores=scores)

if __name__ == "__main__":
    app.run()
