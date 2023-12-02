 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  articles = [
    {
      'id': 1,
      'title': 'New Toy Released',
      'content': 'A new toy has been released that is sure to be a hit with kids. The toy is called the "XYZ" and it is a [description of the toy].'
    },
    {
      'id': 2,
      'title': 'Toy Recall',
      'content': 'A popular toy has been recalled due to a safety hazard. The toy is called the "ABC" and it has been recalled because [description of the safety hazard].'
    },
    {
      'id': 3,
      'title': 'New Toy Store Opens',
      'content': 'A new toy store has opened in town. The store is called "The Toy Box" and it is located at [address].'
    }
  ]
  return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
  articles = [
    {
      'id': 1,
      'title': 'New Toy Released',
      'content': 'A new toy has been released that is sure to be a hit with kids. The toy is called the "XYZ" and it is a [description of the toy].'
    },
    {
      'id': 2,
      'title': 'Toy Recall',
      'content': 'A popular toy has been recalled due to a safety hazard. The toy is called the "ABC" and it has been recalled because [description of the safety hazard].'
    },
    {
      'id': 3,
      'title': 'New Toy Store Opens',
      'content': 'A new toy store has opened in town. The store is called "The Toy Box" and it is located at [address].'
    }
  ]
  article = articles[article_id - 1]
  return render_template('article.html', article=article)

if __name__ == '__main__':
  app.run(debug=True)
