from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_send_sms():
    response = client.post("/sms/v1/send",
    headers={"X-Token": "coneofsilence"}, json={"phone": "+201274472123", "body":"test"})
    assert response.status_code == 200
    assert response.json() == {"message": "sms has been sent"}
