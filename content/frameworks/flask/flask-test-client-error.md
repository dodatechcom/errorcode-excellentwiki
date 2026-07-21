---
title: "[Solution] Flask Test Client Error"
description: "Fix Flask test client errors when testing endpoints fails due to context or configuration issues."
frameworks: ["flask"]
error-types: ["test-error"]
severities: ["error"]
---

Flask test client errors occur when the test application context is not properly configured or when test setup and teardown are incorrect.

## Common Causes

- Test client created before app is fully configured
- Missing test configuration class
- Database not reset between tests
- Authentication not properly mocked in tests
- CSRF protection not disabled for tests

## How to Fix

### Set Up Test Client Properly

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

### Handle Database in Tests

```python
@pytest.fixture
def db_session(app):
    with app.app_context():
        db.create_all()
        yield db.session
        db.session.remove()
        db.drop_all()
```

### Disable CSRF in Tests

```python
@pytest.fixture
def client(app):
    app.config["WTF_CSRF_ENABLED"] = False
    return app.test_client()
```

## Examples

```python
from flask import Flask

app = Flask(__name__)
client = app.test_client()

# Bug -- no test configuration
def test_without_config():
    response = client.get("/")  # May fail with config errors

# Fix -- proper test setup
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "test-key"

def test_with_config():
    response = client.get("/")
    assert response.status_code == 200
```
