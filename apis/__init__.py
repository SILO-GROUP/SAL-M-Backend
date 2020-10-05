from flask_restplus import Api
from .portfolioresource import api as portfolio_namespace


api = Api(
    title="SAL/M Backend API",
    description="Systems Architecture Lifecycle Management",
    version="0.1"
)

api.add_namespace( portfolio_namespace )