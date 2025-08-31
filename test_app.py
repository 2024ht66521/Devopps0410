import pytest
from app import app, workouts

@pytest.fixture(autouse=True)
def clear_workouts():
    # Clear shared state before each test
    workouts.clear()
    yield
    workouts.clear()

def test_get_empty_workouts():
    client = app.test_client()
    r = client.get('/api/workouts')
    assert r.status_code == 200
    assert r.get_json() == []

def test_add_workout_json():
    client = app.test_client()
    payload = {'workout': 'Pushups', 'duration': 15}
    r = client.post('/api/workouts', json=payload)
    assert r.status_code == 201
    data = r.get_json()
    assert data['workout'] == 'Pushups'
    assert data['duration'] == 15

    # verify persisted in list
    r2 = client.get('/api/workouts')
    assert r2.status_code == 200
    assert len(r2.get_json()) == 1

def test_add_workout_form():
    client = app.test_client()
    r = client.post('/api/workouts', data={'workout': 'Run', 'duration': '30'})
    assert r.status_code == 201
    data = r.get_json()
    assert data['workout'] == 'Run'
    assert data['duration'] == 30

def test_bad_duration():
    client = app.test_client()
    r = client.post('/api/workouts', json={'workout': 'X', 'duration': 'abc'})
    assert r.status_code == 400
