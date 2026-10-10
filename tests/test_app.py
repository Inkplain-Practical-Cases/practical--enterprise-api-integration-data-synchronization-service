# Contract tests: validate both accepted and rejected tenant-scoped payloads.
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_accepts_valid_request():
    r = client.post("/sync", json={"tenant_id": "tenant-a", "source_id": "example"})
    assert r.status_code == 200
    assert r.json()["status"] == "accepted"
    assert r.json()["tenant_id"] == "tenant-a"
def test_rejects_invalid_input():
    assert client.post("/sync", json={"tenant_id": "", "source_id": "example"}).status_code == 422
    assert client.post("/sync", json={"tenant_id": "tenant-a", "source_id": ""}).status_code == 422
