# STEP-2 regression: the full API path invokes all cumulative capabilities.
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_end_to_end():
    r = client.post("/sync", json={"tenant_id":"t1","source_id":"s1"})
    assert r.status_code == 200
    assert r.json()["status"] == "accepted"
    assert "pages_fetched" in r.json()
    assert r.json()["pages_fetched"] == 2

def test_rejects_empty_tenant():
    assert client.post("/sync", json={"tenant_id":"","source_id":"s1"}).status_code == 422
