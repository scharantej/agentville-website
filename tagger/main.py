 
from flask import Flask, render_template, request, redirect, url_for
from gcp_tagging import tag_project, untag_project

app = Flask(__name__)

@app.route('/')
def index():
  projects = get_projects()
  opportunities = get_opportunities()
  return render_template('index.html', projects=projects, opportunities=opportunities)

@app.route('/tag', methods=['POST'])
def tag():
  project_id = request.form['project_id']
  opportunity_id = request.form['opportunity_id']
  tag_project(project_id, opportunity_id)
  return redirect(url_for('index'))

@app.route('/untag', methods=['POST'])
def untag():
  project_id = request.form['project_id']
  untag_project(project_id)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
