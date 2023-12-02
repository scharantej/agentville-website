 
from flask import Flask, render_template, request, redirect, url_for
from gcp_projects import get_projects, add_tag, remove_tag

app = Flask(__name__)

@app.route('/')
def index():
  projects = get_projects()
  return render_template('index.html', projects=projects)

@app.route('/add_tag', methods=['POST'])
def add_tag():
  project_id = request.form['project_id']
  salesforce_opportunity_id = request.form['salesforce_opportunity_id']
  add_tag(project_id, salesforce_opportunity_id)
  return redirect(url_for('index'))

@app.route('/remove_tag/<project_id>')
def remove_tag(project_id):
  remove_tag(project_id)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
