---
title: "[Solution] Flask SQLAlchemy Relationship Error"
description: "Fix Flask SQLAlchemy relationship errors when eager/lazy loading fails or causes N+1 query problems."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

SQLAlchemy relationship errors occur when relationships are not properly configured, causing missing data or performance issues.

## Common Causes

- Lazy loading causes N+1 query problems
- Eager loading not configured for frequently accessed relationships
- Backref name conflicts between models
- Foreign key not properly defined
- Relationship cascade not configured

## How to Fix

### Configure Eager Loading

```python
from sqlalchemy.orm import joinedload

users = User.query.options(joinedload(User.posts)).all()
```

### Use Relationship Options

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship(
        "Post",
        backref="author",
        lazy="dynamic",  # or "joined", "subquery"
        cascade="all, delete-orphan",
    )
```

### Optimize Queries

```python
# Instead of N+1 queries
users = User.query.all()
for user in users:
    print(user.posts)  # Additional query for each user

# Use eager loading
users = User.query.options(joinedload(User.posts)).all()
for user in users:
    print(user.posts)  # No additional queries
```

## Examples

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = db.relationship("Book", backref="author", lazy="select")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

# Bug -- N+1 query
authors = Author.query.all()
for author in authors:
    print(author.books)  # Query for each author

# Fix -- eager load
from sqlalchemy.orm import joinedload
authors = Author.query.options(joinedload(Author.books)).all()
```
