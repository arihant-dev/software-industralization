
import pytest
from datetime import datetime
from FlaskWebProject1 import app
import FlaskWebProject1.views as views

@pytest.fixture
def client():
    """Set up the Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home Page' in response.data  # Check if the title exists
    assert str(datetime.now().year).encode() in response.data  # Check the year

def test_home_route_alias(client):
    """Test the /home route."""
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Home Page' in response.data  # Check if the title exists
    assert str(datetime.now().year).encode() in response.data  # Check the year

def test_contact_route(client):
    """Test the contact route."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact' in response.data  # Check if the title exists
    assert b'Your contact page.' in response.data  # Check the message
    assert str(datetime.now().year).encode() in response.data  # Check the year

def test_nonexistent_route(client):
    """Test a nonexistent route."""
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_db_route(client, monkeypatch):
    """Test the /db route."""
    fake_time = datetime(2024, 1, 2, 3, 4, 5)

    class FakeCursor:
        def execute(self, query):
            self.query = query

        def fetchone(self):
            return (fake_time,)

        def close(self):
            return None

    class FakeConnection:
        def cursor(self):
            return FakeCursor()

        def close(self):
            return None

    def fake_get_db_connection():
        return FakeConnection()

    monkeypatch.setattr(views, "get_db_connection", fake_get_db_connection)

    response = client.get('/db')
    assert response.status_code == 200
    assert response.get_json() == {"db_time": fake_time.isoformat()}
