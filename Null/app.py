 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/create_item', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        item = request.form['item']
        items.append(item)
        return redirect(url_for('index'))
    else:
        return render_template('create_item.html')

@app.route('/view_item/<int:item_id>')
def view_item(item_id):
    item = items[item_id]
    return render_template('view_item.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
