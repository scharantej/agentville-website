 
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kidsnewsfeed.db'
db = SQLAlchemy(app)

class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return '<Article %r>' % self.title

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)

  def __repr__(self):
    return '<User %r>' % self.username

@app.route("/")
def index():
  articles = Article.query.all()
  return render_template("index.html", articles=articles)

@app.route("/article/<int:article_id>")
def article(article_id):
  article = Article.query.get(article_id)
  return render_template("article.html", article=article)

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username, password=password).first()
    if user:
      login_user(user)
      return redirect("/")
    else:
      return render_template("login.html", error="Invalid credentials")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  else:
    username = request.form["username"]
    password = request.form["password"]
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
  app.run()
