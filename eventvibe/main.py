 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'New Music from Billie Eilish',
            'content': 'Billie Eilish has released a new song called "Everything I Wanted". The song is about her relationship with her brother, Finneas O'Connell.',
            'url': 'https://www.youtube.com/watch?v=4y-Ysf0f76M'
        },
        {
            'title': 'Shawn Mendes and Camila Cabello Release New Song',
            'content': 'Shawn Mendes and Camila Cabello have released a new song called "Señorita". The song is a duet about a summer romance.',
            'url': 'https://www.youtube.com/watch?v=Pkh8UtuejGw'
        },
        {
            'title': 'Taylor Swift Announces New Album',
            'content': 'Taylor Swift has announced that she will be releasing a new album called "Lover" on August 23rd. The album is her first since 2017's "Reputation".',
            'url': 'https://www.taylorswift.com/lover'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    articles = [
        {
            'title': 'New Music from Billie Eilish',
            'content': 'Billie Eilish has released a new song called "Everything I Wanted". The song is about her relationship with her brother, Finneas O'Connell.',
            'url': 'https://www.youtube.com/watch?v=4y-Ysf0f76M'
        },
        {
            'title': 'Shawn Mendes and Camila Cabello Release New Song',
            'content': 'Shawn Mendes and Camila Cabello have released a new song called "Señorita". The song is a duet about a summer romance.',
            'url': 'https://www.youtube.com/watch?v=Pkh8UtuejGw'
        },
        {
            'title': 'Taylor Swift Announces New Album',
            'content': 'Taylor Swift has announced that she will be releasing a new album called "Lover" on August 23rd. The album is her first since 2017's "Reputation".',
            'url': 'https://www.taylorswift.com/lover'
        }
    ]
    article = articles[article_id]
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
