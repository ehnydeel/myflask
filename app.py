# app.py

from flask import Flask

from config import development as config
from api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return 'Index page'

if __name__ == '__main__':
    app.run(host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG)