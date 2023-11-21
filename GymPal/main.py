 
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Create a database of workouts.
workouts = []

# Create a list of exercises.
exercises = ['Bench Press', 'Squat', 'Deadlift', 'Overhead Press', 'Barbell Row']

# Create a list of preset workouts.
preset_workouts = []

# Home page
@app.route('/')
def home():
  return render_template('index.html', workouts=workouts)

# Add a workout
@app.route('/add_workout', methods=['GET', 'POST'])
def add_workout():
  if request.method == 'POST':
    workout = {
      'date': request.form.get('date'),
      'exercise': request.form.get('exercise'),
      'reps': request.form.get('reps'),
      'sets': request.form.get('sets'),
      'weight': request.form.get('weight')
    }
    workouts.append(workout)
    return redirect(url_for('home'))
  else:
    return render_template('add_workout.html', exercises=exercises)

# View a workout
@app.route('/view_workout/<int:workout_id>')
def view_workout(workout_id):
  workout = workouts[workout_id]
  return render_template('view_workout.html', workout=workout)

# Edit a workout
@app.route('/edit_workout/<int:workout_id>', methods=['GET', 'POST'])
def edit_workout(workout_id):
  workout = workouts[workout_id]
  if request.method == 'POST':
    workout['date'] = request.form.get('date')
    workout['exercise'] = request.form.get('exercise')
    workout['reps'] = request.form.get('reps')
    workout['sets'] = request.form.get('sets')
    workout['weight'] = request.form.get('weight')
    return redirect(url_for('home'))
  else:
    return render_template('edit_workout.html', workout=workout, exercises=exercises)

# Delete a workout
@app.route('/delete_workout/<int:workout_id>')
def delete_workout(workout_id):
  workouts.pop(workout_id)
  return redirect(url_for('home'))

# View trends
@app.route('/view_trends')
def view_trends():
  return render_template('view_trends.html', workouts=workouts)

# Create a preset workout
@app.route('/create_preset', methods=['GET', 'POST'])
def create_preset():
  if request.method == 'POST':
    preset_workout = {
      'name': request.form.get('name'),
      'exercises': request.form.getlist('exercises')
    }
    preset_workouts.append(preset_workout)
    return redirect(url_for('home'))
  else:
    return render_template('create_preset.html', exercises=exercises)

# Edit a preset workout
@app.route('/edit_preset/<int:preset_workout_id>', methods=['GET', 'POST'])
def edit_preset(preset_workout_id):
  preset_workout = preset_workouts[preset_workout_id]
  if request.method == 'POST':
    preset_workout['name'] = request.form.get('name')
    preset_workout['exercises'] = request.form.getlist('exercises')
    return redirect(url_for('home'))
  else:
    return render_template('edit_preset.html', preset_workout=preset_workout, exercises=exercises)

# Delete a preset workout
@app.route('/delete_preset/<int:preset_workout_id>')
def delete_preset(preset_workout_id):
  preset_workouts.pop(preset_workout_id)
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)
