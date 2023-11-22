 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'New Music Festival Announced for Teenagers',
            'content': 'A new music festival for teenagers has been announced. The festival will be held in July in Los Angeles, California. The lineup includes some of the biggest names in teen music, including Justin Bieber, Ariana Grande, and Shawn Mendes.',
            'image': 'https://i.imgur.com/5a64y9G.jpg'
        },
        {
            'title': 'Teen Singer-Songwriter Releases New Album',
            'content': 'A new album from teen singer-songwriter Billie Eilish has been released. The album, titled "When We All Fall Asleep, Where Do We Go?", is Eilish's debut album. It has been met with critical acclaim and has already topped the charts in several countries.',
            'image': 'https://i.imgur.com/6t8349G.jpg'
        },
        {
            'title': 'New Music Video from Teen Pop Star',
            'content': 'A new music video from teen pop star JoJo Siwa has been released. The video, for the song "D.R.E.A.M.", is a high-energy dance routine that is sure to get you moving. The video has already been viewed over 10 million times on YouTube.',
            'image': 'https://i.imgur.com/7y94y9G.jpg'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    articles = [
        {
            'title': 'New Music Festival Announced for Teenagers',
            'content': 'A new music festival for teenagers has been announced. The festival will be held in July in Los Angeles, California. The lineup includes some of the biggest names in teen music, including Justin Bieber, Ariana Grande, and Shawn Mendes.',
            'image': 'https://i.imgur.com/5a64y9G.jpg'
        },
        {
            'title': 'Teen Singer-Songwriter Releases New Album',
            'content': 'A new album from teen singer-songwriter Billie Eilish has been released. The album, titled "When We All Fall Asleep, Where Do We Go?", is Eilish's debut album. It has been met with critical acclaim and has already topped the charts in several countries.',
            'image': 'https://i.imgur.com/6t8349G.jpg'
        },
        {
            'title': 'New Music Video from Teen Pop Star',
            'content': 'A new music video from teen pop star JoJo Siwa has been released. The video, for the song "D.R.E.A.M.", is a high-energy dance routine that is sure to get you moving. The video has already been viewed over 10 million times on YouTube.',
            'image': 'https://i.imgur.com/7y94y9G.jpg'
        }
    ]
    article = articles[article_id]
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
