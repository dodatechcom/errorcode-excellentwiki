---
title: "[Solution] Flask Database Migration Error"
description: "Fix Flask database migration errors when Alembic migrations fail to generate, apply, or detect model changes."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

Database migration errors occur when Alembic cannot detect model changes, generates incorrect migrations, or fails to apply them.

## Common Causes

- Models not imported before migration generation
- Database URI not configured for migrations
- Migration conflict between branches
- Downgrade operation not implemented
- Model changes not saved before migration

## How to Fix

### Initialize Migrations

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

### Generate and Apply Migrations

```bash
# Initialize
flask db init

# Generate migration
flask db migrate -m "add user table"

# Apply
flask db upgrade

# Rollback
flask db downgrade
```

### Handle Migration Conflicts

```bash
# Check heads
flask db heads

# Merge
flask db merge head1 head2
```

## Examples

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# Bug -- model defined but not imported in migration context
# flask db migrate may not detect changes

# Fix -- ensure model is imported
from app.models import User
```
