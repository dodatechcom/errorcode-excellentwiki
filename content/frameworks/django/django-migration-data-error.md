---
title: "[Solution] Django Migration Data Error"
description: "Migration data not migrated."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration data not migrated.

## Common Causes

Wrong migration.

## How to Fix

Use data migration.

## Example

```python
from django.db import migrations
def forwards(apps, schema_editor):
    User = apps.get_model('myapp', 'User')
    User.objects.create(name='admin')
```
