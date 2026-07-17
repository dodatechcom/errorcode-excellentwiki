---
title: "Flask-Migrate Migration Error"
description: "Flask-Migrate raises errors during database migration operations such as migration generation, upgrade, or downgrade"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-Migrate errors occur during database migration operations. These errors typically arise from Alembic (the migration tool underlying Flask-Migrate) and indicate issues with migration scripts, schema conflicts, or database state mismatches.

## Common Causes

- Migration script has conflicting operations
- Database schema is out of sync with migration history
- Model changes not reflected in migration script
- Circular dependency in migration chain
- Missing migration directory or version table

## How to Fix

Regenerate migrations if the auto-generated script is incorrect:

```bash
flask db migrate -m "descriptive message"
```

If migrations are corrupted, stamp the database and regenerate:

```bash
flask db stamp head  # Mark current schema as up-to-date
flask db migrate -m "reset migrations"
flask db upgrade
```

Handle non-reversible migrations:

```python
def upgrade():
    op.add_column('user', db.Column('email', db.String(120), nullable=True))

def downgrade():
    op.drop_column('user', 'email')
```

Fix conflicting migrations by merging heads:

```bash
flask db merge heads
flask db upgrade
```

Ensure the migration environment is initialized:

```bash
flask db init
```

## Examples

```bash
$ flask db migrate -m "add email column"
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) relation "user" does not exist
```

```bash
$ flask db upgrade
alembic.util.exc.CommandError: Can't locate revision identified by 'abc123'
```

## Related Errors

- [SQLAlchemy error]({{< relref "/frameworks/flask/sqlalchemy-error" >}})
- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
