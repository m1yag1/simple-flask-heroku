from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for

app = Flask(__name__)

data = [
    {
        'id': 1,
        'text': 'This was how the deployment went today.',
        'img_url': 'https://media.giphy.com/media/cEkC21ujTN2XC/giphy.gif'
    },
    {
        'id': 2,
        'text': 'When you become the Taco King of PySlackers',
        'img_url': 'https://media.giphy.com/media/4MTFfpZWD91KM/giphy.gif'
    },
{
        'id': 3,
        'text': 'stuff',
        'img_url': ''
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
