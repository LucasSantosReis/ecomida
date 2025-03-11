from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, Base, engine
from app.models import User

def setup_module():
    Base.metadata.create_all(bind=engine)

def teardown_module():
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_create_user():
    username = "test_user"
    password = "test_password"
    db = SessionLocal()
    user = User.create_user(username, password, db)
    db.close()

    db = SessionLocal()
    created_user = db.query(User).filter(User.username == username).first()
    db.close()

    assert created_user is not None
    assert created_user.username == username
    assert created_user.verify_password(password)
