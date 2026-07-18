---
title: "[Solution] Flask-Migrate Error — How to Fix"
description: "Fix Flask-Migrate errors. Resolve Alembic migration failures, database version, and migration conflicts."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask-Migrate error occurs when Alembic-based migrations fail to generate, apply, or manage database schema changes. Flask-Migrate wraps Alembic for Flask applications and shares many of its common issues.

## Why It Happens

Flask-Migrate uses Alembic under the hood. Errors occur when the migration repository is not initialized, when `FLASK_APP` is not set, when database models are out of sync with migration files, when Alembic cannot detect changes, or when migration dependencies conflict.

## Common Error Messages

```
flask_migrate.cli.MigrateError: No such command 'db'
```

```
alembic.util.exc.CommandError: Can't locate revision identified by 'abc123'
```

```
sqlalchemy.exc.OperationalError: table "users" already exists
```

```
alembic.util.exc.CommandError: Multiple head revisions
```

## How to Fix It

### 1. Initialize Migrations Properly

Set up Flask-Migrate correctly:

```python
# app.py
from flask import Flask
from flask_migrate import Migrate
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    return app
```

```bash
# Set FLASK_APP
export FLASK_APP=app.py

# Initialize migrations
flask db init

# Generate initial migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade
```

### 2. Resolve Conflicting Migrations

When multiple heads exist:

```bash
# Check current heads
flask db heads

# Merge conflicting heads
flask db merge heads

# Apply merged migration
flask db upgrade
```

```python
# The generated merge migration looks like:
def upgrade():
    # Merged migration
    pass

def downgrade():
    pass
```

### 3. Fix "Table Already Exists" Errors

When the database has tables but no migration history:

```bash
# Option 1: Stamp the current schema
flask db stamp head

# Option 2: Create migration from existing schema
flask db migrate --autogenerate -m "Detect existing tables"
flask db upgrade

# Option 3: Fake-apply a migration
flask db upgrade --fake
```

### 4. Handle Autogenerate Limitations

Alembic autogenerate doesn't detect all changes. Manually edit migration files for:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add column with default value
    op.add_column('users', sa.Column('status', sa.String(20), nullable=False, server_default='active'))

    # Rename column (not autodetected)
    op.alter_column('users', 'name', new_column_name='full_name')

    # Create index
    op.create_index('ix_users_email', 'users', ['email'], unique=True)

    # Add foreign key
    op.create_foreign_key('fk_posts_author', 'posts', 'users', ['author_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_posts_author', 'posts', type_='foreignkey')
    op.drop_index('ix_users_email', 'users')
    op.drop_column('users', 'status')
```

## Common Scenarios

**Scenario 1: `flask db migrate` produces empty migration.**
This happens when models are defined in a module that isn't imported. Ensure models are imported in the `__init__.py` or `models.py` file that's loaded by the app.

**Scenario 2: Migration fails on PostgreSQL but works on SQLite.**
Different databases have different SQL syntax. Test migrations against your production database engine, not just SQLite.

**Scenario 3: Downgrade fails with data loss.**
Alembic doesn't reverse data migrations. Write explicit downgrade functions and test them before deploying.

## Prevent It

1. **Always run `flask db migrate --autogenerate`** instead of `flask db migrate` to ensure Alembic detects actual model changes.

2. **Review generated migrations before applying.** Check the generated SQL for accuracy and add missing operations.

3. **Keep migration files in version control.** Never delete migration files that have been applied to production.
