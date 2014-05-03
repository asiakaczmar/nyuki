from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    context = {'text': 'Hello'}
    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(debug=True)



