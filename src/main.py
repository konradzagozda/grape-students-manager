from flask import Flask
from database import db

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:postgres@postgres/students_manager"
db.init_app(app) 


with app.app_context():
    db.create_all()