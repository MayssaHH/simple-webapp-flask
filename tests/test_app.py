import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app


def test_root_route_returns_200():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
