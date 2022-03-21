from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_send_email():
    response = client.post("/email/v1/send-email",
    headers={"X-Token": "coneofsilence"}, json={"subject": "foobar", "email": ["brehan.ibrahim@gmail.com"], "body": {"title":"The Foo Barters","name":"test"}})
    assert response.status_code == 200
    assert response.json() == {"message": "email has been sent"}

def test_send_email_background():
    response = client.post("/email/v1/send-email/backgroundtasks",
    headers={"X-Token": "coneofsilence"}, json={"subject": "foobar", "email": ["brehan.ibrahim@gmail.com"], "body": {"title":"The Foo Barters","name":"test"}})
    assert response.status_code == 200
    assert response.json() == {"message": "email has been sent"}

