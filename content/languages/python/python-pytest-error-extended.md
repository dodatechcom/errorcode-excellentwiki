---
title: "[Solution] Python pytest Extended Error — Test Runner Failures"
description: "Fix Python pytest errors like fixture errors, parametrize failures, marker errors, and plugin conflicts. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 432
---

# Python pytest Extended Error — Test Runner Failures

pytest errors occur when fixtures are misconfigured, parametrize arguments don't match, markers are not registered, or plugins conflict with each other. These are common in complex test suites.

## Common Causes

```python
# fixture not found: name mismatch
import pytest

@pytest.fixture
def setup_data():
    return {"key": "value"}

def test_something(setup):  # typo: should be setup_data
    assert setup["key"] == "value"

# FixtureScopeMismatch: fixture used in wrong scope
@pytest.fixture(scope="session")
def db_connection():
    return create_connection()

@pytest.fixture
def db_cursor(db_connection):  # function scope uses session fixture
    return db_connection.cursor()

# parametrize argument mismatch
@pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])
def test_add(a, b, c):  # c not provided by parametrize
    assert a + b == c

# PytestUnknownMarkUsageError: unregistered marker
@pytest.mark.slow
def test_heavy_computation():
    pass

# Plugin conflict: duplicate plugin registration
# conftest.py in both root and tests/ with same fixture names
```

## How to Fix

### Fix 1: Match Fixture Names Exactly
Ensure fixture names in test signatures match defined fixture names.
```python
import pytest

@pytest.fixture
def setup_data():
    return {"key": "value"}

def test_something(setup_data):  # correct fixture name
    assert setup_data["key"] == "value"
```

### Fix 2: Respect Fixture Scopes
Use fixtures with compatible scopes.
```python
import pytest

@pytest.fixture(scope="session")
def db_connection():
    return create_connection()

@pytest.fixture
def db_cursor(db_connection):  # function scope, uses session fixture - OK
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()
```

### Fix 3: Align Parametrize Arguments with Test Parameters
Ensure parametrize provides values for all test parameters.
```python
import pytest

@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (3, 4, 7)])
def test_add(a, b, expected):
    assert a + b == expected
```

### Fix 4: Register Custom Markers
Register custom markers in pytest configuration.
```ini
# pytest.ini or pyproject.toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow",
    "integration: marks integration tests",
]
```
```toml
# pyproject.toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow",
    "integration: marks integration tests",
]
```

### Fix 5: Use Unique Fixture Names Across conftest Files
Avoid name collisions between conftest.py files.
```python
# tests/unit/conftest.py
@pytest.fixture
def unit_db():
    return create_test_db()

# tests/integration/conftest.py
@pytest.fixture
def integration_db():
    return create_real_db()
```

## Examples

```python
# Advanced parametrize with indirect fixtures
import pytest

@pytest.fixture
def database(request):
    db = create_connection(request.param)
    yield db
    db.close()

@pytest.mark.parametrize("database", ["sqlite", "postgres"], indirect=True)
def test_database_operations(database):
    assert database.is_connected()

# Parametrize with ids for readable output
@pytest.mark.parametrize(
    "input,expected",
    [
        (1, 2),
        (2, 4),
        (3, 6),
    ],
    ids=["odd", "even", "odd"],
)
def test_double(input, expected):
    assert input * 2 == expected
```

## Related Errors

- [Python Loguru Error](/languages/python/python-loguru-error/)
- [Python Pydantic Error](/languages/python/python-pydantic-error/)
- [Python FastAPI Error](/languages/python/python-fastapi-error/)
