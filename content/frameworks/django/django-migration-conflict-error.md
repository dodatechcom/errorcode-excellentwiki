---
title: "[Solution] Django Migration Conflict Error"
description: "Conflicting migrations."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Conflicting migrations.

## Common Causes

Parallel migrations.

## How to Fix

Merge.

## Example

```bash
python manage.py makemigrations --merge
```
