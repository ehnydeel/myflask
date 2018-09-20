# app.py

from flask import Flask, Blueprint

from config import Server
from meintest import meintest
from api import api

app = Flask(__name__)
srvConfig = Server()

app.register_blueprint(meintest, url_prefix='/meintest')
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return 'Index page'

if __name__ == '__main__':
    app.run(host=srvConfig.host,
            port=srvConfig.port,
            debug=srvConfig.debug)