from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, {__name__}'

@app.route('/hs')
def hello_hs():
    return f'Hello, hs'

@app.route('/jjangu')
def hello_jjangu():
    return f'<b> JJANGU <b>'