---
title: "TemplateSyntaxError: Invalid block tag"
description: "Django raises TemplateSyntaxError when a template contains an invalid or unrecognized block tag."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Django's template engine encounters a block tag it does not recognize, or when a known tag is used with incorrect syntax.

## Common Causes

- Typo in a template tag name (e.g. `{% stat %}` instead of `{% static %}`)
- Using a tag that requires an `{% endtag %}` but omitting the closing tag
- Nesting block tags incorrectly (e.g. placing an `{% if %}` inside another `{% if %}` without closing the inner one first)
- Using Django 2+ syntax on an older version of Django

## How to Fix

Check the template file for the line number reported in the traceback and correct the tag syntax:

```html
{# Wrong — typo in tag name #}
{% loadt static %}

{# Correct #}
{% load static %}
```

Make sure every opening block tag has a matching closing tag:

```html
{# Wrong — missing endif #}
{% if user.is_active %}
  <p>Welcome</p>

{# Correct #}
{% if user.is_active %}
  <p>Welcome</p>
{% endif %}
```

## Example

```python
# views.py
from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"name": "World"})
```

```html
<!-- home.html -->
<h1>Hello {% upper name %}</h1>
<!-- ^ "upper" is not a valid block tag — should be {{ name|upper }} -->
```

## Related Errors

- [django.db.utils.OperationalError: table already exists]({{< relref "/frameworks/django/migration-error" >}})
