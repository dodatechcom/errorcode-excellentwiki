---
title: "[Solution] Python Django Migration Error — How to Fix"
description: "Fix Python Django migration and ORM errors. Resolve model, migration, and database issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Django Migration Error

A `django.db.utils.OperationalError` occurs when Django migrations fail when model fields don't match the existing database schema or migrations conflict..

## Why It Happens

This happens when migrations are out of sync with the database, model fields have changed, or conflicting migrations exist. Python enforces strict type and state checking.

## Common Error Messages

- `relation does not exist`
- `Cannot resolve keyword`
- `Conflicting migrations detected`
- `duplicate key value violates unique constraint`

## How to Fix It

### Fix 1: Fix migration conflicts

```python
python manage.py makemigrations --merge
python manage.py migrate
```

### Fix 2: Handle model field changes

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
```

### Fix 3: Fix query lookups

```python
from django.db.models import Q

users = User.objects.filter(
    Q(name__icontains='alice') | Q(email__endswith='@example.com')
)
```

### Fix 4: Handle database operations

```python
from django.db import transaction

@transaction.atomic
def create_user_with_profile(data):
    user = User.objects.create(**data)
    Profile.objects.create(user=user)
    return user
```

## Common Scenarios

- **Field type changes** — Changing CharField to TextField creates migration.
- **Many-to-many relations** — Adding through model requires careful migration.
- **Data migration** — Custom migrations that transform existing data.

## Prevent It

- Always run makemigrations before migrate
- Use transaction.atomic() for rollback support
- Test migrations with python manage.py migrate --plan

## Related Errors

- - [OperationalError](/languages/python/operationalerror/) — database operation failed
- - [FieldError](/languages/python/fielderror/) — invalid field lookup
- - [IntegrityError](/languages/python/integrityerror/) — constraint violation
