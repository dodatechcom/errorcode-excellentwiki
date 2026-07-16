---
title: "AuthenticationFailed: authentication failed"
description: "Django raises AuthenticationFailed when the authentication backend rejects the credentials"
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["authentication", "login", "session", "permission"]
weight: 5
---

This error occurs when Django's authentication system rejects a login attempt due to invalid credentials, disabled accounts, or misconfigured authentication backends.

## Common Causes

- Incorrect username or password
- User account is inactive (`is_active=False`)
- Authentication backend is misconfigured in `AUTHENTICATION_BACKENDS`
- Custom user model with non-standard username field

## How to Fix

1. Use Django's built-in authentication functions:

```python
from django.contrib.auth import authenticate, login

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request, "login.html", {"error": "Invalid credentials"})
```

2. Check authentication backends in settings:

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
```

3. For custom user models, ensure the backend supports it:

```python
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
```

## Examples

```python
from django.contrib.auth import authenticate

user = authenticate(request, username="admin", password="wrong")
user  # None
# Attempting to login with user=None causes AuthenticationFailed
```

```text
django.contrib.auth.models.User.DoesNotExist: User matching query does not exist.
```

## Related Errors

- [ValidationError]({{< relref "/frameworks/django/form-error" >}})
