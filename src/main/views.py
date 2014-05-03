import os
from flask import Flask, render_template

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../app')

app = Flask(__name__, static_folder=ASSETS_DIR)


@app.route('/')
def hello():
    context = {'text': 'Hello'}
    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(debug=True)