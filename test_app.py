from app import app

def test_health():
    client = app.test_client()
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json == {"status": "healthy"}

def test_predict_even():
    client = app.test_client()
    res = client.get('/predict?number=4')
    assert res.json == {"number": 4, "type": "even"}

def test_predict_odd():
    client = app.test_client()
    res = client.get('/predict?number=5')
    assert res.json == {"number": 5, "type": "odd"}

