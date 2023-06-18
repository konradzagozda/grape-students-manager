from flask_restx import Api

api = Api(
    version="1.0",
    prefix="/api/v1",
    title="Students Manager",
    description="Students Manager",
    doc="/swagger/",
)