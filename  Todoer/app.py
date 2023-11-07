 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        todo = request.form['todo']
        todos.append(todo)
        return redirect(url_for('index'))
    return render_template('add_todo.html')

@app.route('/edit_todo/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    if request.method == 'POST':
        todo = request.form['todo']
        todos[todo_id] = todo
        return redirect(url_for('index'))
    return render_template('edit_todo.html', todo_id=todo_id, todo=todos[todo_id])

@app.route('/delete_todo/<int:todo_id>')
def delete_todo(todo_id):
    del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
