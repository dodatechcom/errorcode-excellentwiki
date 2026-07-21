---
title: "[Solution] Django RunSQL Error"
description: "RunSQL migration failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

RunSQL migration failing.

## Common Causes

Wrong SQL.

## How to Fix

Check SQL.

## Example

```python
migrations.RunSQL('INSERT INTO users (name) VALUES ("admin")', 'DELETE FROM users WHERE name="admin"')
```
