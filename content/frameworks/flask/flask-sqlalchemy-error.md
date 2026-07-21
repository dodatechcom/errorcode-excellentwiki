---
title: "[Solution] Flask SQLAlchemy Session Error -- How to Fix"
description: "Fix Flask SQLAlchemy session errors. Resolve database session management, connection, and query issues."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask SQLAlchemy session error occurs when the database session is misused, connections are not properly managed, or transactions are left open. SQLAlchemy's session management is critical for data integrity.

## Why It Happens

SQLAlchemy sessions are scoped to the request lifecycle in Flask. Errors occur when sessions are not committed, when stale sessions are reused across requests, when the session is accessed outside the request context, when connections are exhausted, or when models reference tables that don't exist.

## Common Error Messages

```
sqlalchemy.exc.InvalidRequestError: Session's data has been expired; commit the session before accessing
```

```
sqlalchemy.exc.OperationalError: (OperationalError) could not connect to server
```

```
sqlalchemy.exc.IntegrityError: (IntegrityError) NOT NULL constraint failed
```

```
sqlalchemy.exc.ResourceClosedError: This transaction is closed
```

## How to Fix It

### 1. Initialize SQLAlchemy Properly

Use the correct initialization pattern:

```python
# extensions.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# app.py
from flask import Flask
from extensions import db
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from . import models  # Import models here

    return app
```

### 2. Handle Sessions in Views

Commit and close sessions correctly:

```python
from flask import request, jsonify
from extensions import db
from models import User

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    user = User(
        email=data['email'],
        name=data['name'],
    )

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)

    db.session.commit()
    return jsonify(user.to_dict())
```

### 3. Avoid Session Expired Errors

Handle lazy-loaded relationships carefully:

```python
# Problem: Session expired after commit
user = User.query.first()
db.session.commit()  # After this, user is expired
print(user.name)     # InvalidRequestError!

# Solution 1: Use joinedload for relationships
from sqlalchemy.orm import joinedload

users = User.query.options(joinedload(User.profile)).all()

# Solution 2: Refresh the object
db.session.refresh(user)
print(user.name)

# Solution 3: Merge detached objects
user = db.session.merge(user)
```

### 4. Use Connection Pooling

Configure connection pool settings:

```python
# settings.py
SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/db'
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 20
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = 1800  # Recycle connections after 30 minutes
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Common Scenarios

**Scenario 1: `db.session.commit()` not called.**
If you modify objects but don't commit, changes are lost when the session closes. Always call `db.session.commit()` after modifications.

**Scenario 2: Concurrent request session conflicts.**
In multi-threaded servers, each request should have its own session. Flask-SQLAlchemy handles this with scoped sessions, but raw SQLAlchemy needs explicit scoping.

**Scenario 3: Bulk operations cause memory issues.**
Use `bulk_insert_mappings()` or `bulk_update_mappings()` for large datasets instead of creating individual objects:

```python
# Instead of this (slow)
for data in large_list:
    user = User(**data)
    db.session.add(user)

# Use this (fast)
db.session.bulk_insert_mappings(User, large_list)
db.session.commit()
```

## Prevent It

1. **Always call `db.session.commit()` after modifications** and `db.session.rollback()` in exception handlers.

2. **Use `SQLALCHEMY_TRACK_MODIFICATIONS = False`** to avoid Flask deprecation warnings and reduce memory usage.

3. **Close sessions explicitly in background tasks** that don't use Flask's request lifecycle.
