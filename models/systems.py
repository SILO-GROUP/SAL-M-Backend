from flask_restplus import Api, fields

model_system = Api.model(
    'System Model',
    {
        'name': fields.String(
            required=True,
            description="Name of the system being created.",
            help="Name cannot be blank."
        )
    }
)