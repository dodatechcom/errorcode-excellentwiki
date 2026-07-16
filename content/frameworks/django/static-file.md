---
title: "StaticFilesWarning: 404 for static file"
description: "Django raises an error when a template requests a static file that cannot be found by the static file finders"
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["static", "404", "staticfiles", "css", "javascript"]
weight: 5
---

This error occurs when Django cannot locate a static file referenced in a template. The `{% static %}` tag or `STATIC_URL` path resolves to a 404 because the file does not exist in any configured static directory.

## Common Causes

- File does not exist in any of the `STATICFILES_DIRS` directories
- Typo in the filename or path
- `staticfiles` app is not in `INSTALLED_APPS`
- Missing `collectstatic` step in production

## How to Fix

1. Verify the file exists in a static directory:

```python
from django.contrib.staticfiles.finders import find
find("css/style.css")
```

2. Add static file directories to settings:

```python
# settings.py
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "assets",
]
```

3. Run `collectstatic` for production:

```bash
python manage.py collectstatic --noinput
```

4. Use the `{% static %}` tag correctly in templates:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

## Examples

```html
<!-- Template references a missing file -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/nonexistent.css' %}">
```

```text
ResourceWarning: Static file 'css/nonexistent.css' not found.
```

## Related Errors

- [TemplateSyntaxError: Invalid block tag]({{< relref "/frameworks/django/template-error" >}})
