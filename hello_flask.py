from flask import Flask, render_template
from book_example import test_sin

app = Flask(__name__)


@app.route('/')
def abcd():
    return '1234'


@app.route('/test')
def test():
    return str(test_sin())


app.run()
