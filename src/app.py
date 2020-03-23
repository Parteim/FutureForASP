### library  ==========
from flask import Flask

### local   ===========
from config import Configuration
from general.bluprint import app as main_app

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(main_app, url_prefix='/')
