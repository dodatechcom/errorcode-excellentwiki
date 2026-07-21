---
title: "[Solution] Flask SQLAlchemy Query Error"
description: "Fix Flask SQLAlchemy query errors when database queries return incorrect results or fail."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

SQLAlchemy query errors occur when queries are syntactically incorrect, use wrong column names, or return unexpected results.

## Common Causes

- Query uses wrong column name
- Filter conditions are incorrect
- Missing `db.session.commit()` after changes
- Query result not properly paginated
- Complex joins not properly configured

## How to Fix

### Write Correct Queries

```python
# Simple filter
users = User.query.filter_by(name="Alice").first()

# Complex filter
users = User.query.filter(
    User.name.contains("test"),
    User.active == True,
).order_by(User.name).all()

# Pagination
page = User.query.paginate(page=1, per_page=20)
```

### Handle Query Results

```python
@app.route("/users")
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)

    pagination = User.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False,
    )

    return {
        "users": [u.to_dict() for u in pagination.items],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
    }
```

### Use Proper Joins

```python
from sqlalchemy.orm import joinedload

users = User.query.options(
    joinedload(User.posts),
    joinedload(User.profile),
).all()
```

## Examples

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Bug -- wrong column name
users = User.query.filter_by(username="Alice").all()  # AttributeError

# Fix -- use correct column name
users = User.query.filter_by(name="Alice").all()
```
