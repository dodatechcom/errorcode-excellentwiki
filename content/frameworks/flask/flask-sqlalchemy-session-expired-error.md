---
title: "[Solution] Flask SQLAlchemy Session Expired Error"
description: "Fix Flask SQLAlchemy session expired errors when accessing detached objects after commit."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

After committing a SQLAlchemy session, accessing lazy-loaded attributes on objects causes `DetachedInstanceError` because the object is no longer associated with the session.

## Common Causes

- Accessing relationship attributes after session commit
- Session closed but object still referenced
- Using `expire_on_commit=True` with detached objects
- Accessing object attributes in templates after commit
- Object serialized before attributes are loaded

## How to Fix

### Use `expire_on_commit=False`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"expire_on_commit": False})
```

### Eager Load Relationships

```python
from sqlalchemy.orm import joinedload

users = User.query.options(joinedload(User.posts)).all()
```

### Access Attributes Before Commit

```python
@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    name = user.name  # Access before commit
    db.session.commit()
    return {"name": name}
```

## Examples

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    db.session.commit()
    return {"name": user.name}  # DetachedInstanceError

# Fix -- access before commit
@app.route("/user/<int:user_id>")
def get_user_fixed(user_id):
    user = User.query.get(user_id)
    name = user.name  # Access before commit
    db.session.commit()
    return {"name": name}
```
