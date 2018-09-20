# app.py

# import third-party modules
from flask import Flask

# import local modules
from config import development as config
from api import api

# create flask-application
app = Flask(__name__)

# ROUTING - register blueprint-routes
app.register_blueprint(api, url_prefix='/api')

# ROUTING - setup entrypoint-route
@app.route('/')
def index():
    return 'Index page'

# START FLASK-APPLICATION
if __name__ == '__main__':
    app.run(host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG)