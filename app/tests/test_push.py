from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.conn.db import Base
from app.router.push import get_db
from app.config import get_settings
import random

settings = get_settings()

DATABASE_URL = f'mysql+mysqlconnector://{settings.db_user}:{settings.db_pass}@{settings.db_host}/{settings.db_schema_test}'
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_register_user():
    response = client.post("push/v1/register",json={"user_id": random.randint(1,100),"token":"fkjfkf","device_info":{}})
    assert response.status_code == 201
