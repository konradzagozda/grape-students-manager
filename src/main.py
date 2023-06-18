from flask import Flask
from flask_restx import Api
from models import db
from resources import student_ns

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:postgres@postgres/students_manager"

api = Api(
    version="1.0",
    prefix="/api/v1",
    title="Students Manager",
    description="Students Manager",
    doc="/swagger/",
)

api.add_namespace(student_ns)

db.init_app(app) 
api.init_app(app)

with app.app_context():
    db.create_all()