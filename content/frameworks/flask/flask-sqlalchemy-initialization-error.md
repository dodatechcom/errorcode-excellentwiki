---
title: "[Solution] Flask SQLAlchemy Initialization Error"
description: "Fix Flask SQLAlchemy initialization errors when database models fail to load or tables are not created."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

SQLAlchemy initialization errors occur when the database is not properly configured or models are not imported before table creation.

## Common Causes

- `SQLALCHEMY_DATABASE_URI` not set
- Models imported after `db.create_all()`
- Database driver not installed
- Connection pool exhausted
- Migration not applied after model changes

## How to Fix

### Initialize SQLAlchemy Properly

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
```

### Import Models Before Creating Tables

```python
from app.models import User, Post  # Import models first

with app.app_context():
    db.create_all()
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

# Bug -- no database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)  # Fails when querying

# Fix -- set database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)
```
