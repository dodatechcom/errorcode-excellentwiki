---
title: "[Solution] FastAPI Template Error -- How to Fix"
description: "Fix FastAPI template errors. Resolve Jinja2 template rendering and missing variable issues."
frameworks: ["fastapi"]
error-types: ["template-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI template error occurs when Jinja2 templates fail to render due to missing variables, syntax errors, or misconfiguration.

## Why It Happens

Template errors happen due to undefined variables, incorrect syntax, missing files, or template engine misconfiguration.

## Common Error Messages

```
jinja2.exceptions.UndefinedError: 'username' is undefined
```

```
jinja2.exceptions.TemplateNotFound: base.html
```

```
jinja2.exceptions.TemplateSyntaxError: unexpected end of template
```

```
FileNotFoundError: Template directory not found
```

## How to Fix It

### 1. Set Up Jinja2 Templates

Configure template engine.

```python
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

@app.get('/items/{item_id}')
async def read_item(request: Request, item_id: str):
    return templates.TemplateResponse('item.html', {
        'request': request,
        'item_id': item_id,
        'item': get_item(item_id)
    })
```

### 2. Handle Missing Variables

Use default values or conditional checks.

```html
{# Use default filter #}
<p>{{ user.name | default('Anonymous') }}</p>

{# Check if variable exists #}
{% if user is defined %}
  <p>Hello, {{ user.name }}</p>
{% endif %}
```

### 3. Use Template Inheritance

Create base templates with blocks.

```html
{# templates/base.html #}
<html>
<head><title>{% block title %}Default{% endblock %}</title></head>
<body>{% block content %}{% endblock %}</body>
</html>

{# templates/home.html #}
{% extends 'base.html' %}
{% block title %}Home{% endblock %}
{% block content %}<h1>Welcome</h1>{% endblock %}
```

### 4. Add Template Error Handling

Handle rendering errors.

```python
@app.exception_handler(500)
async def template_error_handler(request, exc):
    return templates.TemplateResponse('error.html', {
        'request': request, 'error': str(exc)
    }, status_code=500)
```

## Common Scenarios

**Scenario 1: Template renders blank.**
Check all required variables are passed.

**Scenario 2: Template file not found.**
Verify the template directory path.

**Scenario 3: Template syntax error.**
Check for unclosed blocks.

## Prevent It

1. **Use template linting.**
Validate Jinja2 syntax before deploy.

2. **Provide default values.**
Use `default` filter for optional vars.

3. **Write template tests.**
Test rendering with expected content.

