 
from flask import Flask, render_template, request

app = Flask(__name__)

questions = []
answers = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        question = request.form['question']
        questions.append(question)
    return render_template('questions.html', questions=questions)

@app.route('/answers', methods=['GET', 'POST'])
def answers():
    if request.method == 'POST':
        answer = request.form['answer']
        answers.append(answer)
    return render_template('answers.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
