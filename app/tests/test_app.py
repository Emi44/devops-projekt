from src.app import app

def test_health_endpoint():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"

def test_hello_endpoint():
    client = app.test_client()
    r = client.get("/hello")
    assert r.status_code == 200
    assert "Hello" in r.get_data(as_text=True)

def test_version_endpoint():
    client = app.test_client()
    r = client.get("/version")
    assert r.status_code == 200
    assert r.json["app"] == "devops-projekt"
