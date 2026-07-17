---
title: "[Solution] Django NoReverseMatch — URL pattern not found"
description: "Fix Django NoReverseMatch errors. Resolve URL pattern not found issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["url", "noreversematch", "pattern", "reverse", "django"]
weight: 5
---

A NoReverseMatch error occurs when Django cannot find a URL pattern matching the given name and arguments. The URL name may be incorrect or missing required parameters.

## Common Causes

- URL name does not exist in urls.py
- Required URL parameters are missing
- App namespace not specified
- URL pattern was renamed or removed
- Wrong app namespace in template

## How to Fix

### Check URL Configuration

```python
# urls.py
urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
]
```

### Reverse URL in Python

```python
from django.urls import reverse
url = reverse('post-detail', kwargs={'pk': 1})
```

### Reverse URL in Template

```html
<a href="{% url 'myapp:post-detail' pk=1 %}">Link</a>
```

### Check URL Names

```bash
python manage.py show_urls
```

### Verify Namespace

```python
# urls.py
app_name = 'myapp'
urlpatterns = [...]
```

## Examples

```python
# Example 1: Missing parameter
reverse('post-detail')
# NoReverseMatch: Reverse for 'post-detail' with arguments '()' keyword arguments '{}' not found
# Fix: reverse('post-detail', kwargs={'pk': 1})

# Example 2: Wrong namespace
{% url 'post-detail' pk=1 %}
# Fix: {% url 'myapp:post-detail' pk=1 %}
```

## Related Errors

- [Django URL Error]({{< relref "/frameworks/django/django-url-error" >}}) — URL configuration issues
- [Django Template Error]({{< relref "/frameworks/django/django-template-error" >}}) — template rendering error
