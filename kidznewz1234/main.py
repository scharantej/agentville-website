 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/live")
def live():
  return render_template("live.html")

@app.route("/articles")
def articles():
  return render_template("articles.html")

@app.route("/games")
def games():
  return render_template("games.html")

if __name__ == "__main__":
  app.run()
