---
title: "[Solution] Django CSRF Verification Failed"
description: "Fix Django CSRF verification failed errors. Resolve CSRF token issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["csrf", "token", "forbidden", "middleware", "django"]
weight: 5
---

A CSRF verification failed error occurs when Django's CSRF protection middleware rejects a POST, PUT, or DELETE request because the CSRF token is missing or invalid.

## Common Causes

- `{% csrf_token %}` template tag missing from form
- CSRF cookie not set (first request was GET, not POST)
- Cross-origin request without proper CORS configuration
- Form action URL points to a different domain
- `CSRF_COOKIE_SECURE` set but request is not HTTPS

## How to Fix

### Add CSRF Token to Form

```html
<form method="post" action="/submit/">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

### Exclude View from CSRF

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_api_view(request):
    ...
```

### Check CSRF Settings

```python
CSRF_COOKIE_SECURE = True  # for HTTPS
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = ['https://example.com']
```

### AJAX Requests

```javascript
// Get cookie value
const csrftoken = document.cookie.split('; ')
    .find(row => row.startsWith('csrftoken='))
    .split('=')[1];

fetch('/api/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
    },
    body: data,
});
```

## Examples

```python
# Example 1: Missing template tag
# 403 Forbidden: CSRF verification failed
# Fix: add {% csrf_token %} to form

# Example 2: Cross-origin request
# Fix: add domain to CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = ['https://api.example.com']
```

## Related Errors

- [Django Permission Error]({{< relref "/frameworks/django/django-permission-error" >}}) — PermissionDenied
- [Django Form Error]({{< relref "/frameworks/django/django-form-error" >}}) — form validation error
