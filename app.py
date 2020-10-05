# workaround for a known bug in werkzeug
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask
from apis import api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

api.init_app( app )

if __name__ == '__main__':
    app.run()
