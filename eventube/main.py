 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'New Music Festival Announced for Teenagers',
            'content': 'A new music festival for teenagers has been announced. The festival will be held in July in Los Angeles, California. The lineup includes some of the biggest names in teen music, including Justin Bieber, Ariana Grande, and Shawn Mendes.',
        },
        {
            'title': 'Teenagers React to New Music Video',
            'content': 'A new music video from a popular teen artist has been released. The video has been met with mixed reactions from teenagers. Some teenagers love the video, while others think it is too provocative.',
        },
        {
            'title': 'Teenagers Speak Out About Their Favorite Music',
            'content': 'A new survey has revealed the favorite music of teenagers. The survey found that pop music is the most popular genre among teenagers, followed by hip-hop and rock music.',
        },
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
    app.run()
