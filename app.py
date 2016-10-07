from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for

app = Flask(__name__)

data = [
    {
        'id': 1,
        'text': 'That drink is nasty',
        'img_url': 'https://67.media.tumblr.com/c2910f5eaf259d33a8f3f5d1f1f70e42'
                   '/tumblr_odjoplUm701s373hwo1_250.gif'
    },
{
        'id': 2,
        'text': 'What I feel like when it\'s friday',
        'img_url': 'https://67.media.tumblr.com/9e5cbc54bc8ebf2f5e49900861a81426'
                   '/tumblr_odqr13OKYS1s373hwo1_250.gif'
    }
]


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='img/favicon.ico'))


@app.route('/')
def index():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
