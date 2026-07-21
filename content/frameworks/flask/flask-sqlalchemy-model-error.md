---
title: "[Solution] Flask SQLAlchemy Model Error"
description: "Fix Flask SQLAlchemy model errors when defining or querying database models fails."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

SQLAlchemy model errors occur when model definitions are incorrect, relationships are misconfigured, or queries fail.

## Common Causes

- Model does not inherit from `db.Model`
- Missing primary key definition
- Relationship backref not properly configured
- Query uses wrong column names
- Model not registered with the database

## How to Fix

### Define Models Correctly

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
```

### Query Models Correctly

```python
# Get by ID
user = User.query.get(42)

# Filter
users = User.query.filter_by(name="Alice").all()

# Complex query
users = User.query.filter(User.name.contains("test")).order_by(User.name).all()
```

### Handle Relationship Queries

```python
user = User.query.get(1)
posts = user.posts  # Access related posts
```

## Examples

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Bug -- missing primary key
class BadModel(db.Model):
    name = db.Column(db.String(100))  # No primary key

# Fix -- add primary key
class GoodModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
```
