---
title: "SQLAlchemy Error in Flask"
description: "Flask-SQLAlchemy raises OperationalError, ProgrammingError, or IntegrityError when database operations fail"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sqlalchemy", "database", "orm", "sql", "flask"]
weight: 5
---

## What This Error Means

SQLAlchemy errors in Flask-SQLAlchemy occur when database operations fail due to connection issues, invalid SQL, missing tables, constraint violations, or configuration problems. These errors are typically raised as `sqlalchemy.exc.OperationalError`, `ProgrammingError`, or `IntegrityError`.

## Common Causes

- Database connection string misconfigured
- Database server not running or unreachable
- Table does not exist (model not created)
- Unique constraint violation (duplicate data)
- Invalid SQL query or relationship configuration

## How to Fix

Verify your database configuration:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

Create database tables before using them:

```python
with app.app_context():
    db.create_all()
```

Handle integrity errors gracefully:

```python
from sqlalchemy.exc import IntegrityError

@app.route('/create_user', methods=['POST'])
def create_user():
    user = User(username=request.form['username'])
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash('Username already exists')
        return redirect(url_for('create_user'))
    return redirect(url_for('profile', id=user.id))
```

Use migrations for schema changes:

```bash
flask db init
flask db migrate -m "add users table"
flask db upgrade
```

Check for missing relationships:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
```

## Examples

```python
user = User.query.filter_by(username='admin').first()
# ProgrammingError: relation "user" does not exist
```

```text
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" failed
```

## Related Errors

- [Import error]({{< relref "/frameworks/flask/import-error" >}})
- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
