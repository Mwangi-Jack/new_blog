from flask import  render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = [
        {
            'author': {'username': 'Becky'},
            'body': "it is such a lovely day"
        },
        {
            'author': {'username': 'charles'},
            'body': 'Look who is back!'

        }
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)
