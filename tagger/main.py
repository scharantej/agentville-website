 
from flask import Flask, render_template, request

app = Flask(__name__)

projects = [
    {'id': 'project-1', 'name': 'Project 1'},
    {'id': 'project-2', 'name': 'Project 2'},
    {'id': 'project-3', 'name': 'Project 3'},
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/tag_project', methods=['POST'])
def tag_project():
    project_id = request.form['project_id']
    salesforce_id = request.form['salesforce_id']

    # TODO: Save the salesforce ID for the project

    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
