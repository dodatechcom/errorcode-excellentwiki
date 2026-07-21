---
title: "[Solution] Flask Reloader Error"
description: "Debug reloader not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Debug reloader not working.

## Common Causes

Wrong path.

## How to Fix

Check FLASK_APP.

## Example

```bash
FLASK_APP=app.py flask run
```
