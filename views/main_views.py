from flask import Blueprint

# Blueprint 클래스를 통해 객체를 만듬
bp = Blueprint('main',__name__, url_prefix='/')

@bp.route('/')
def hello():
    return f'Hello, {__name__}'

@bp.route('/hs')
def hello_hs():
    return f'Hello, hs'

@bp.route('/jjangu')
def hello_jjangu():
    return f'<b> JJANGU <b>'
    