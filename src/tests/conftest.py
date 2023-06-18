import pytest
from main import app as flask_app
from main import db as _db

@pytest.fixture
def app():
    return flask_app

@pytest.fixture
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.remove()
        _db.drop_all()