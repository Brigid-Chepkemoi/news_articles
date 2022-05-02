from flask import Flask
from flask_bootstrap import Bootstrap

from app.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
bootstrap = Bootstrap(app)