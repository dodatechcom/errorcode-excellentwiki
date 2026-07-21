---
title: "[Solution] Flask SQLAlchemy Session Close Error"
description: "Fix Flask SQLAlchemy session close errors when database connections are not properly released."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

Flask-SQLAlchemy session close errors occur when database connections are not properly released after use, leading to connection pool exhaustion.

## Common Causes

- Session not closed after request completes
- `db.session.rollback()` not called on exceptions
- Connection pool size exceeded due to leaked connections
- Using `db.session.remove()` at wrong time
- Background tasks holding sessions open

## How to Fix

### Use Proper Session Management

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
```

### Handle Exceptions in Database Operations

```python
@app.route("/users")
def get_users():
    try:
        users = User.query.all()
        db.session.commit()
        return jsonify([u.to_dict() for u in users])
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
```

### Configure Connection Pool

```python
app.config["SQLALCHEMY_POOL_SIZE"] = 10
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800
```

## Examples

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Bug -- session not cleaned up
@app.route("/create")
def create():
    user = User(name="Alice")
    db.session.add(user)
    db.session.commit()
    return "Created"

# Fix -- handle cleanup
@app.route("/create-fixed")
def create_fixed():
    try:
        user = User(name="Alice")
        db.session.add(user)
        db.session.commit()
        return "Created"
    except Exception:
        db.session.rollback()
        raise
```
