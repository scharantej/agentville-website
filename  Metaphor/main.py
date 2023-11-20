 
from flask import Flask, render_template, request, redirect, url_for
import text_bison

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        project = request.form.get('project')
        dataset = request.form.get('dataset')
        table = request.form.get('table')

        # Send the metadata to the LLM prompt using text-bison
        response = text_bison.generate_column_descriptions(project, dataset, table)

        # Redirect to the results page
        return redirect(url_for('results', response=response))

    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    response = request.args.get('response')

    return render_template('results.html', response=response)

if __name__ == '__main__':
    app.run()


html
<!DOCTYPE html>
<html>
<head>
    <title>BigQuery Column Descriptions</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>BigQuery Column Descriptions</h1>
    <form action="/" method="post">
        <label for="project">Project:</label>
        <input type="text" name="project">
        <br>
        <label for="dataset">Dataset:</label>
        <input type="text" name="dataset">
        <br>
        <label for="table">Table:</label>
        <input type="text" name="table">
        <br>
        <input type="submit" value="Generate Column Descriptions">
    </form>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
    <title>BigQuery Column Descriptions</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>BigQuery Column Descriptions</h1>
    <p>{{ response }}</p>
</body>
</html>
