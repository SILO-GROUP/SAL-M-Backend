# workaround for a known bug in werkzeug
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask
from apis import api


app = Flask(__name__)
api.init_app( app )

if __name__ == '__main__':
    flask_app.run()
