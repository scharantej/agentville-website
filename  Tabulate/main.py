 
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table', methods=['GET', 'POST'])
def table():
    if request.method == 'POST':
        # Get the data from the form
        data = request.form.get('data')

        # Convert the data to a Pandas DataFrame
        df = pd.read_csv(data)

        # Render the table
        return render_template('table.html', df=df)

    else:
        # Render the form
        return render_template('table.html')

if __name__ == '__main__':
    app.run(debug=True)


index.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Table of Data</title>
</head>
<body>
    <h1>Table of Data</h1>
    <form action="/table" method="post">
        <input type="file" name="data">
        <input type="submit" value="Submit">
    </form>
</body>
</html>


table.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Table of Data</title>
</head>
<body>
    <h1>Table of Data</h1>
    <table>
        <thead>
            <tr>
                <th></th>
                {% for column in df.columns %}
                    <th>{{ column }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in df.iterrows() %}
                <tr>
                    <td>{{ row[0] }}</td>
                    {% for column in row[1] %}
                        <td>{{ column }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
