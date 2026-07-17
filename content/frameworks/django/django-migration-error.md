---
title: "[Solution] Django Migration Error — migration error"
description: "Fix Django migration errors. Resolve database migration failures."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["migrations", "database", "migrate", "schema", "django"]
weight: 5
---

A Django migration error occurs when a database migration fails to apply. This can be caused by schema conflicts, missing dependencies, or database state issues.

## Common Causes

- Migration conflicts between branches
- Table already exists from manual creation
- Missing migration for model changes
- Database backend incompatibility
- Circular migration dependencies

## How to Fix

### Check Migration Status

```bash
python manage.py showmigrations
```

### Detect Conflicts

```bash
python manage.py makemigrations --check
```

### Fake a Migration

```bash
python manage.py migrate <app_name> <migration_number> --fake
```

### Squash Migrations

```bash
python manage.py squashmigrations <app_name> 0001 0005
```

### Reset Migrations (development only)

```bash
python manage.py migrate <app_name> zero
python manage.py migrate
```

## Examples

```bash
# Example 1: Migration conflict
python manage.py makemigrations
# Error: Conflicting migrations detected
# Fix: python manage.py makemigrations --merge

# Example 2: Table already exists
python manage.py migrate
# django.db.utils.OperationalError: table already exists
# Fix: python manage.py migrate <app> <number> --fake
```

## Related Errors

- [Django Settings Error]({{< relref "/frameworks/django/django-settings-error" >}}) — ImproperlyConfigured
- [Django Database Error]({{< relref "/frameworks/django/django-db-connection" >}}) — DatabaseError connection failed
