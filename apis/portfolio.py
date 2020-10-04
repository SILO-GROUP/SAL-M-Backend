from flask_restplus import Namespace, Resource, fields
from models.systems import model_system

api = Namespace('portfolio', description='Portfolio Item Lifecycle')


@api.route('/system')
class Portfolio(Resource):
    def get(self):
        return { "status": "got new data" }

    @api.expect( model_system )
    def post(self):

        return { "status": "posted new data" }
