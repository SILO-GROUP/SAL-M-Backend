from flask_restplus import Namespace, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

api = Namespace('portfolio', description='Portfolio Item Lifecycle')

db = SQLAlchemy()


ma = Marshmallow( api )

# also swagger?
model_system = api.model(
    'System Model',
    {
        'name': fields.String(
            required=True,
            description="Name of the system.",
            help="Name cannot be blank."
        ),
        'description': fields.String(
            required=False,
            description="Description of the system.",
            help="Must be at most 255 chars."
        )
    }
)


# db model
class SystemDBModel(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 255 ) )
    description = db.Column( db.String( 255 ) )

    def __repr__(self):
        return '<SystemModel %s>' % self.name


# marshmallow schema (swagger?)
class SystemMASchema(ma.Schema):
    class Meta:
        fields = ( "id", "name", "description" )
        model = SystemDBModel


system_schema = SystemMASchema()
systems_schema = SystemMASchema(many=True)

# CRUD
# PUT - UPDATE
# DELETE - DELETE
# POST - CREATE
# GET - FETCH

@api.route('/system')
class PortfolioResource(Resource):
    def get(self):
        systems = SystemDBModel.query.all()
        # retrieve system resources from the portfolio
        return systems_schema.dump( systems )

    @api.expect( model_system )
    def post(self):
        # create a new system resource in the portfolio
        return { "status": "created a new system" }

    def delete(self):
        return { "status": "deleted a system" }


api.add_resource( PortfolioResource )