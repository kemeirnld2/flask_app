from flask import Flask, render_template, request, url_for, flash, redirect

# ...

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)
# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')