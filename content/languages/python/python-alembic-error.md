---
title: "[Solution] Python Alembic Migration Error — How to Fix"
description: "Fix Python Alembic migration errors. Resolve merge conflicts, head detection failures, and downgrade issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Alembic Migration Error

An `alembic.util.exc.CommandError` or `sqlalchemy.exc.OperationalError` occurs when Alembic fails to detect the current migration head, encounters conflicting migration branches, or when migration scripts contain invalid operations.

## Why It Happens

Alembic manages database schema migrations. Errors arise when multiple heads exist without merging, when migration scripts reference non-existent tables, when downgrades remove columns that other migrations depend on, or when the alembic_version table is corrupted.

## Common Error Messages

- `CommandError: Multiple head revisions are present`
- `alembic.util.exc.CommandError: Can't locate revision identified by`
- `sqlalchemy.exc.OperationalError: relation does not exist`
- `CommandError: The following revision(s) are not part of the`

## How to Fix It

### Fix 1: Handle multiple heads

```python
# Wrong — not merging migration branches
# alembic upgrade head  # fails with multiple heads

# Correct — merge heads before upgrading
# alembic merge heads
# alembic upgrade head

# Or in code:
from alembic import command
command.upgrade(config, "heads")
command.merge(config, "heads")
command.upgrade(config, "head")
```

### Fix 2: Fix migration script errors

```python
# alembic/versions/001_create_users.py
from alembic import op
import sqlalchemy as sa

# Wrong — not handling existing data
# op.add_column("users", sa.Column("email", sa.String(255), nullable=False))

# Correct — add column with default first
def upgrade():
    op.add_column("users", sa.Column("email", sa.String(255), server_default=""))
    op.alter_column("users", "email", nullable=False)

def downgrade():
    op.drop_column("users", "email")
```

### Fix 3: Fix head detection

```python
# Wrong — stale alembic_version table
# SELECT * FROM alembic_version returns deleted revision

# Correct — reset version table
# alembic downgrade base
# alembic stamp head

# Or manually fix
from alembic import command
from alembic.config import Config

config = Config("alembic.ini")
command.upgrade(config, "base")
command.stamp(config, "head")
```

### Fix 4: Handle data migrations

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create new column
    op.add_column("users", sa.Column("full_name", sa.String(255)))

    # Migrate data
    conn = op.get_bind()
    conn.execute(
        sa.text("UPDATE users SET full_name = first_name || ' ' || last_name")
    )

    # Remove old columns
    op.drop_column("users", "first_name")
    op.drop_column("users", "last_name")

def downgrade():
    op.add_column("users", sa.Column("first_name", sa.String(100)))
    op.add_column("users", sa.Column("last_name", sa.String(100)))
    op.drop_column("users", "full_name")
```

## Common Scenarios

- **Multiple heads** — Two developers create migrations from the same base, creating parallel branches.
- **Missing column** — Migration adds a column that a subsequent migration assumes already exists.
- **Downgrade failure** — Downgrade removes a column that other migrations reference.

## Prevent It

- Always run `alembic merge heads` before creating new migrations.
- Test both upgrade and downgrade paths before committing migration scripts.
- Use `alembic history --indicate-dependencies` to visualize migration dependencies.

## Related Errors

- [CommandError](/languages/python/alembic-error/) — Alembic command failed
- [OperationalError](/languages/python/operationalerror/) — database operation failed
- [MultipleHeadsError](/languages/python/multiple-heads/) — migration branches not merged
