 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grammar')
def grammar():
    return render_template('grammar.html')

@app.route('/vocabulary')
def vocabulary():
    return render_template('vocabulary.html')

@app.route('/conversation')
def conversation():
    return render_template('conversation.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run()
