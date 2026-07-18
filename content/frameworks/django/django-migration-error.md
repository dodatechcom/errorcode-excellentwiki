---
title: "[Solution] Django Migration Failed or Conflicting Error — How to Fix"
description: "Fix Django migration errors. Resolve migration conflicts, failed migrations, and database schema issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django migration error occurs when database migrations fail to apply, conflict with each other, or become inconsistent with the actual database schema. These errors can block deployments and development workflows.

## Why It Happens

Django migrations track schema changes through a `django_migrations` table. Errors arise when multiple developers create conflicting migrations, when migrations reference models or fields that no longer exist, when a migration partially applies and then fails, or when the database schema drifts from what Django expects.

## Common Error Messages

```
django.db.migrations.exceptions.InconsistentMigrationHistory
```

```
django.db.utils.OperationalError: table "myapp_article" already exists
```

```
Migration myapp.0005_auto_20240101_0000 is applied before its dependency
```

```
LookupError: No installed app with label 'myapp'
```

## How to Fix It

### 1. Resolve Migration Conflicts

When multiple migration branches conflict, squash them:

```bash
# Check for conflicts
python manage.py showmigrations --plan

# Squash migrations in the app
python manage.py squashmigrations myapp 0001 0010

# Review the squashed migration file, then apply
python manage.py migrate
```

### 2. Fix Inconsistent Migration History

When the database has applied migrations that Django doesn't know about:

```python
# Option 1: Fake-apply the missing migration
python manage.py migrate myapp 0005 --fake

# Option 2: Fake all pending migrations
python manage.py migrate --fake

# Option 3: Reset migration history (dangerous — backup first)
python manage.py migrate myapp zero
python manage.py migrate myapp
```

### 3. Handle Partially Applied Migrations

When a migration fails mid-way, the database may be in an inconsistent state:

```bash
# Check migration status
python manage.py showmigrations myapp

# If a migration is partially applied, manually fix the database
python manage.py dbshell

# In the database shell, check what was applied
SELECT * FROM django_migrations WHERE app='myapp';

# Remove the failed migration record
DELETE FROM django_migrations WHERE app='myapp' AND name='0005_auto_20240101';

# Then re-run
python manage.py migrate myapp 0005
```

### 4. Recreate Migrations from Scratch

When migrations are too broken to fix:

```bash
# Backup your database first!
python manage.py dumpdata > backup.json

# Remove all migration files (keep __init__.py)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Recreate migrations
python manage.py makemigrations

# Fake-apply since tables already exist
python manage.py migrate --fake

# Verify
python manage.py showmigrations
```

## Common Scenarios

**Scenario 1: New developer on team gets migration errors.**
This happens when the team has multiple uncommitted migration branches. The new developer should pull the latest code, then run `python manage.py migrate` to apply the combined migrations.

**Scenario 2: Migration references deleted model.**
If you delete a model but a migration still references it, `migrate` will fail. Create a new migration that removes the model's table, or edit the problematic migration to remove the reference.

**Scenario 3: Production database has manual schema changes.**
If someone altered the database directly (added columns, changed types), Django's migrations will conflict. Use `makemigrations --check` to detect drift and create corrective migrations.

## Prevent It

1. **Always create migrations in a single branch.** Avoid having multiple developers create migrations simultaneously. Merge and apply migrations before creating new ones.

2. **Never edit migration files after they are applied.** Instead, create a new migration that makes the correction. This keeps the migration history consistent.

3. **Run `python manage.py migrate --plan` before applying migrations** to review what changes will be made to the database.
