---
title: "django.db.utils.OperationalError: table already exists"
description: "Django raises this OperationalError when a migration tries to create a database table that already exists."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Django attempts to create a table during a migration but the table already exists in the database. It typically happens when migrations get out of sync with the actual database schema.

## Common Causes

- Manually created a table in the database that conflicts with a migration
- Ran a migration, rolled it back, and tried to re-run it without squashing
- Switched database backends and the new backend has a table with the same name
- The `migrations` table itself is out of sync with applied migrations

## How to Fix

Check which migration is failing and verify the table state:

```bash
python manage.py showmigrations
python manage.py dbshell
-- check if the table exists
```

If the table was created manually, either drop it or fake the migration:

```bash
# Fake the migration so Django thinks it already ran
python manage.py migrate <app_name> <migration_number> --fake
```

If the migration is stale, consider squashing migrations:

```bash
python manage.py squashmigrations <app_name> 0001 0005
```

## Example

```bash
$ python manage.py migrate
django.db.utils.OperationalError: table "app_userprofile" already exists
```

This happens when `0002_auto.py` tries to create `userprofile` but it was already created by a previous manual step or a stale migration file.

## Related Errors

- [TemplateSyntaxError: Invalid block tag]({{< relref "/frameworks/django/template-error" >}})
