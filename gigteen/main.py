 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  events = [
    {
      'id': 1,
      'title': 'Teen Music Festival',
      'description': 'A music festival for teenagers featuring live performances from popular artists.',
      'date': '2023-03-18',
      'time': '12:00 PM - 6:00 PM',
      'location': 'Central Park'
    },
    {
      'id': 2,
      'title': 'Battle of the Bands',
      'description': 'A competition for teenage bands to showcase their talents.',
      'date': '2023-04-01',
      'time': '7:00 PM - 10:00 PM',
      'location': 'The Fillmore'
    },
    {
      'id': 3,
      'title': 'Teen Open Mic Night',
      'description': 'An open mic night for teenagers to perform their own music.',
      'date': '2023-04-15',
      'time': '7:00 PM - 9:00 PM',
      'location': 'The Coffee Bean & Tea Leaf'
    }
  ]
  return render_template('index.html', events=events)

@app.route('/event/<int:event_id>')
def event(event_id):
  event = [
    {
      'id': 1,
      'title': 'Teen Music Festival',
      'description': 'A music festival for teenagers featuring live performances from popular artists.',
      'date': '2023-03-18',
      'time': '12:00 PM - 6:00 PM',
      'location': 'Central Park'
    },
    {
      'id': 2,
      'title': 'Battle of the Bands',
      'description': 'A competition for teenage bands to showcase their talents.',
      'date': '2023-04-01',
      'time': '7:00 PM - 10:00 PM',
      'location': 'The Fillmore'
    },
    {
      'id': 3,
      'title': 'Teen Open Mic Night',
      'description': 'An open mic night for teenagers to perform their own music.',
      'date': '2023-04-15',
      'time': '7:00 PM - 9:00 PM',
      'location': 'The Coffee Bean & Tea Leaf'
    }
  ]
  return render_template('event.html', event=event)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
