---
title: "[Solution] Django CSRF Verification Failed Error — How to Fix"
description: "Fix Django CSRF verification failed errors. Resolve CSRF token missing or incorrect issues in Django forms."
frameworks: ["django"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django CSRF verification failed error occurs when the Cross-Site Request Forgery token is missing, invalid, or does not match the session. This is a security measure that Django enforces on all POST, PUT, PATCH, and DELETE requests.

## Why It Happens

Django's CSRF protection works by embedding a unique token in each form and validating it on submission. The error is triggered when the token is absent from the request, has expired, doesn't match the cookie, or when cookies are blocked by the browser. It is especially common with AJAX requests, API endpoints, and misconfigured middleware.

## Common Error Messages

```
403 Forbidden: CSRF verification failed. Request aborted.
```

```
Reason given for failure: CSRF token missing or incorrect.
```

```
CSRF cookie not set.
```

```
Origin checking failed - https://example.com does not match TrustedOrigins.
```

## How to Fix It

### 1. Add CSRF Token to Templates

Always include the CSRF token tag in Django templates for form submissions:

```html
<form method="post" action="/submit/">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

### 2. Include CSRF Token in AJAX Requests

For JavaScript AJAX calls, read the cookie and include the token in the request header:

```javascript
// Read CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

fetch('/api/submit/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ data: 'value' })
});
```

### 3. Exempt Specific Views

For API views that use token-based authentication instead of CSRF:

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def my_api_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'method not allowed'}, status=405)
```

### 4. Configure Trusted Origins

For cross-origin requests, add your domains to `CSRF_TRUSTED_ORIGINS`:

```python
# settings.py
CSRF_TRUSTED_ORIGINS = [
    'https://example.com',
    'https://www.example.com',
    'https://app.example.com',
]

# For subdomain matching in Django 4.0+
CSRF_TRUSTED_ORIGINS = [
    'https://*.example.com',
]
```

## Common Scenarios

**Scenario 1: AJAX POST request returns 403.**
This happens because AJAX requests don't automatically include the CSRF token. You must extract it from the `csrftoken` cookie and add it as the `X-CSRFToken` header or `csrfmiddlewaretoken` field in the request body.

**Scenario 2: CSRF cookie not set error.**
This occurs when the `CsrfViewMiddleware` cannot set the CSRF cookie. Check that `SessionMiddleware` is listed before `CsrfViewMiddleware` in `MIDDLEWARE`, and that the response is not a redirect that drops the cookie.

**Scenario 3: CSRF fails after domain change.**
When deploying to a new domain, the `CSRF_TRUSTED_ORIGINS` setting must include the new domain. Django 4.0+ requires exact scheme and domain matching.

## Prevent It

1. **Never disable CSRF globally.** Only exempt individual views that genuinely cannot use CSRF tokens, such as third-party API webhooks.

2. **Keep middleware order correct.** Ensure `SessionMiddleware` comes before `CsrfViewMiddleware` in your `MIDDLEWARE` setting, as CSRF depends on the session.

3. **Test CSRF with incognito mode.** Browsers may cache stale CSRF cookies. Always test CSRF-protected forms in an incognito or private browsing window.
