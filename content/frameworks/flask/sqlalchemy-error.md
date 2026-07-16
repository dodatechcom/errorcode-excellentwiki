---
title: "SQLAlchemy error"
description: "Flask-SQLAlchemy raises OperationalError, IntegrityError, or ProgrammingError during database operations"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sqlalchemy", "database", "orm", "session"]
weight: 5
---

This error occurs when Flask-SQLAlchemy encounters a problem executing a database query, such as connection failures, constraint violations, or SQL syntax errors.

## Common Causes

- Database connection URI is misconfigured or unreachable
- Integrity constraint violation (unique, foreign key, not null)
- Query references a table or column that does not exist
- SQLAlchemy session is not properly committed or rolled back

## How to Fix

1. Verify the database URI:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

2. Handle database errors in route handlers:

```python
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

@app.route('/users', methods=['POST'])
def create_user():
    user = User(name=request.form['name'])
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": "User already exists"}, 409
    return {"id": user.id}, 201
```

3. Use `db.session.rollback()` on any error:

```python
try:
    db.session.commit()
except Exception:
    db.session.rollback()
    raise
```

4. Enable query logging for debugging:

```python
import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

## Examples

```python
user = User(name="Alice")
db.session.add(user)
db.session.commit()
# sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation)
# duplicate key value violates unique constraint "users_name_key"
```

## Related Errors

- [Session error]({{< relref "/frameworks/flask/session-error" >}})
