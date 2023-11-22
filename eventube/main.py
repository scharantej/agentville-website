 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'New Music from Billie Eilish',
            'content': 'Billie Eilish has released a new single, "Everything I Wanted." The song is about her relationship with her brother, Finneas O'Connell.',
            'url': 'https://www.billboard.com/articles/news/9360170/billie-eilish-everything-i-wanted-song-lyrics-meaning'
        },
        {
            'title': 'Shawn Mendes and Camila Cabello Release New Song',
            'content': 'Shawn Mendes and Camila Cabello have released a new song, "Señorita." The song is a duet about a summer romance.',
            'url': 'https://www.rollingstone.com/music/music-news/shawn-mendes-camila-cabello-senorita-song-lyrics-meaning-967473/'
        },
        {
            'title': 'Taylor Swift Announces New Album',
            'content': 'Taylor Swift has announced her new album, "Lover." The album is set to be released on August 23rd.',
            'url': 'https://www.usatoday.com/story/entertainment/music/2019/06/13/taylor-swift-announces-new-album-lover-release-date-tracklist/1124266001/'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    articles = [
        {
            'title': 'New Music from Billie Eilish',
            'content': 'Billie Eilish has released a new single, "Everything I Wanted." The song is about her relationship with her brother, Finneas O'Connell.',
            'url': 'https://www.billboard.com/articles/news/9360170/billie-eilish-everything-i-wanted-song-lyrics-meaning'
        },
        {
            'title': 'Shawn Mendes and Camila Cabello Release New Song',
            'content': 'Shawn Mendes and Camila Cabello have released a new song, "Señorita." The song is a duet about a summer romance.',
            'url': 'https://www.rollingstone.com/music/music-news/shawn-mendes-camila-cabello-senorita-song-lyrics-meaning-967473/'
        },
        {
            'title': 'Taylor Swift Announces New Album',
            'content': 'Taylor Swift has announced her new album, "Lover." The album is set to be released on August 23rd.',
            'url': 'https://www.usatoday.com/story/entertainment/music/2019/06/13/taylor-swift-announces-new-album-lover-release-date-tracklist/1124266001/'
        }
    ]
    article = articles[article_id]
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
