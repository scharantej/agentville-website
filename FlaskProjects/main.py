 
from flask import Flask, render_template, request

app = Flask(__name__)

projects = [
  {
    "name": "Project 1",
    "note": "This is a note for Project 1."
  },
  {
    "name": "Project 2",
    "note": None
  },
  {
    "name": "Project 3",
    "note": "This is a note for Project 3."
  }
]

@app.route("/")
def index():
  return render_template("index.html", projects=projects)

@app.route("/add_note", methods=["POST"])
def add_note():
  note = request.form["note"]
  projects[0]["note"] = note
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)
