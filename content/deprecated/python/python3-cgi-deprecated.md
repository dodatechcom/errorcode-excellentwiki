---
title: "[Solution] Deprecated Function Migration: cgi module to modern web frameworks"
description: "Migrate from deprecated cgi module to modern web frameworks."
deprecated_function: "cgi.FieldStorage()"
replacement_function: "Flask/Django request objects"
languages: ["python"]
deprecated_since: "Python 3.11+"
---

# [Solution] Deprecated Function Migration: cgi module to modern web frameworks

The `cgi.FieldStorage()` has been deprecated in favor of `Flask/Django request objects`.

## Migration Guide

cgi module is outdated.

## Before (Deprecated)

```python
import cgi
form = cgi.FieldStorage()
name = form.getvalue('name')
```

## After (Modern)

```python
from flask import request
name = request.form.get('name')
```

## Key Differences

- cgi module is deprecated
