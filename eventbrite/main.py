 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'New Music Festival Announced for Teenagers',
            'content': 'A new music festival for teenagers has been announced. The festival will be held in July in Los Angeles, California. The lineup includes some of the biggest names in teen music, including Justin Bieber, Ariana Grande, and Shawn Mendes.',
            'image': 'https://i.imgur.com/5a64y9u.jpg'
        },
        {
            'title': 'New Album from Teen Pop Sensation',
            'content': 'Teen pop sensation Olivia Rodrigo has released her new album, "Sour". The album is full of catchy songs about heartbreak and teenage angst. It is sure to be a hit with teenagers everywhere.',
            'image': 'https://i.imgur.com/6t8349u.jpg'
        },
        {
            'title': 'New Music Video from Teen Rapper',
            'content': 'Teen rapper Lil Nas X has released his new music video for the song "Montero (Call Me By Your Name)". The video is a visual feast, featuring Lil Nas X in a variety of colorful and eye-catching outfits. It is sure to get you dancing.',
            'image': 'https://i.imgur.com/7u8459u.jpg'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = articles[article_id]
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
