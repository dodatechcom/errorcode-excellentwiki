---
title: "[Solution] Django DatabaseError — connection failed"
description: "Fix Django DatabaseError connection failures. Resolve database connection issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["database", "connection", "db", "OperationalError", "django"]
weight: 5
---

A Django DatabaseError occurs when the application cannot connect to the database or encounters a database operation failure.

## Common Causes

- Database server is not running
- Incorrect database credentials in settings.py
- Database does not exist
- Connection pool exhausted
- Network connectivity issues to database server

## How to Fix

### Check Database Settings

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Test Database Connection

```python
from django.db import connections
conn = connections['default']
conn.ensure_connection()
```

### Run Migrations

```bash
python manage.py migrate
```

### Check Connection Pool

```python
DATABASES['default']['CONN_MAX_AGE'] = 600
```

### Verify Database Exists

```bash
psql -U myuser -d mydb -c "SELECT 1;"
```

## Examples

```bash
# Example 1: Connection refused
python manage.py migrate
# django.db.utils.OperationalError: connection refused
# Fix: start PostgreSQL service

# Example 2: Wrong password
# django.db.utils.OperationalError: FATAL: password authentication failed
# Fix: update DATABASES setting with correct password
```

## Related Errors

- [Django Redis Error]({{< relref "/frameworks/django/django-redis-error" >}}) — Redis connection error
- [Django Transaction Error]({{< relref "/frameworks/django/django-transaction-error" >}}) — TransactionManagementError
