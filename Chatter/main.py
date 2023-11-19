 
# Import the necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

# Define the chat route
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html')
    elif request.method == 'POST':
        message = request.form['message']
        # Save the message to the database
        # ...
        return redirect(url_for('chat'))

# Run the app
if __name__ == '__main__':
    app.run()
