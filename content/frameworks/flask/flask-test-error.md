---
title: "[Solution] Flask Test Error"
description: "Fix Flask test errors when unit or integration tests fail due to context or configuration issues."
frameworks: ["flask"]
error-types: ["test-error"]
severities: ["error"]
---

Flask test errors occur when test setup is incomplete, context is missing, or test configuration differs from production.

## Common Causes

- Test client created before app is configured
- Database not reset between tests
- CSRF protection not disabled for tests
- Authentication not properly mocked
- Test fixtures not properly set up

## How to Fix

### Set Up Test Fixtures

```python
import pytest
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
```

### Reset Database Between Tests

```python
@pytest.fixture(autouse=True)
def reset_db():
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()
```

### Mock External Services

```python
from unittest.mock import patch

def test_with_mock(client):
    with patch("app.services.external_api") as mock_api:
        mock_api.return_value = {"status": "ok"}
        response = client.get("/api/data")
        assert response.status_code == 200
```

## Examples

```python
from flask import Flask

app = Flask(__name__)

# Bug -- no test configuration
client = app.test_client()

def test_without_config():
    response = client.get("/")  # May fail with config errors

# Fix -- set test config
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "test-key"
client = app.test_client()

def test_with_config():
    response = client.get("/")
    assert response.status_code == 200
```
