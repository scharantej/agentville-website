 
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the game page
@app.route('/game')
def game():
    return render_template('game.html')

# Route for handling player moves
@app.route('/move', methods=['POST'])
def move():
    # Get the player's move
    move = request.form.get('move')

    # Update the game state
    game_state = update_game_state(move)

    # Check if the game is over
    if is_game_over(game_state):
        return redirect(url_for('winner'))

    # Redirect the player to the game page
    return redirect(url_for('game'))

# Route for displaying the winner
@app.route('/winner')
def winner():
    return render_template('winner.html')

if __name__ == '__main__':
    app.run()
