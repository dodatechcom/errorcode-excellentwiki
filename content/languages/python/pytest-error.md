---
title: "[Solution] Python Pytest Collection or Fixture Error — How to Fix"
description: "Fix Python Pytest errors. Resolve fixture, collection, and assertion issues with Pytest test framework."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Pytest Collection or Fixture Error

A Pytest error occurs when tests fail to collect, fixtures cannot be resolved, or assertion rewriting fails. Pytest's plugin architecture and fixture system have specific requirements.

## Why It Happens

Pytest collects test files by looking for functions starting with `test_`. Fixtures are resolved by name matching between function parameters and fixture definitions. Errors occur when fixture dependencies are circular, test files have syntax errors, or conftest.py files are misconfigured.

## Common Error Messages

- `ERROR: could not find fixture 'fixture_name'`
- `ERROR: collection error - syntax error in test file`
- `E     fixture 'db' not found`
- `INTERNALERROR> pluggy.manager.PluginValidationError`

## How to Fix It

### Fix 1: Fix fixture dependencies

```python
import pytest

@pytest.fixture
def database():
    db = create_connection()
    yield db
    db.close()

@pytest.fixture
def user(database):
    return database.create_user('Alice')

def test_user_exists(user):
    assert user is not None
```

### Fix 2: Fix conftest.py structure

```python
# conftest.py
import pytest

@pytest.fixture
def shared_resource():
    return {'data': [1, 2, 3]}

# fixtures defined here are available in all test files
# in this directory and subdirectories
```

### Fix 3: Use parametrize for multiple test cases

```python
import pytest

@pytest.mark.parametrize('input,expected', [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

### Fix 4: Fix plugin loading

```python
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ['tests']
addopts = '-v --tb=short'
plugins = ['cov']
```

## Common Scenarios

- **Circular fixture dependencies** — Fixture A depends on B which depends on A.
- **Missing test files** — Pytest cannot collect tests due to import errors.
- **Fixture scope mismatch** — Requesting a session-scoped fixture from a function-scoped one.

## Prevent It

- Use pytest --fixtures to list all available fixtures
- Keep conftest.py files minimal and well-organized
- Run pytest --collect-only to verify test collection before running

## Related Errors

- - [ImportError](/languages/python/importerror/) — module not found
- - [AssertionError](/languages/python/assertionerror/) — assertion failed
