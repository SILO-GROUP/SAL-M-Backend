# workaround for a known bug in werkzeug
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask
from flask_restplus import Api, Resource

from models.systems import model_system

app = Flask(__name__)

api = Api(
    app = flask_app,
    title="SAL/M Backend API",
    description="Systems Architecture Lifecycle Management",
    version="0.1"
)

demo_namespace = api.namespace('demo', description='Demo APIs')

portfolio_namespace = api.namespace('portfolio', description='Portfolio Item Lifecycle')


@demo_namespace.route('/')
class MainClass(Resource):
    def get(self):
        return { "status": "got new data" }

    def post(self):
        return { "status": "posted new data" }


@portfolio_namespace.route('/system')
class Portfolio(Resource):
    def get(self):
        return { "status": "got new data" }

    @portfolio_namespace.expect( model_system )
    def post(self):

        return { "status": "posted new data" }


if __name__ == '__main__':
    flask_app.run()
