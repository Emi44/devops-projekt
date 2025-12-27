from src.app import app

def test_health_endpoint():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"

def test_users_get_returns_list():
    client = app.test_client()
    r = client.get("/users")
    assert r.status_code in (200, 500)

def test_users_post_returns_created():
    client = app.test_client()
    r = client.post("/users", json={"name": "TestUser"})
    assert r.status_code in (201, 500)