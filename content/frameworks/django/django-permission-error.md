---
title: "[Solution] Django PermissionDenied — permission required"
description: "Fix Django PermissionDenied errors. Resolve permission and authorization issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Django PermissionDenied error occurs when a user attempts an action they are not authorized to perform. This raises an `Http403` exception.

## Common Causes

- User lacks the required permission
- `@permission_required` decorator fails
- Object-level permission check fails
- `has_perm()` returns False
- Anonymous user accessing protected view

## How to Fix

### Check User Permissions

```python
user.has_perm('app.permission_name')
user.get_all_permissions()
```

### Use Permission Decorator

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.change_model')
def my_view(request):
    ...
```

### Use Class-Based View Mixin

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'app.change_model'
```

### Custom Permission Check

```python
def has_permission(self, request, obj=None):
    if obj is None:
        return True
    return obj.owner == request.user
```

### Handle 403 Error

```python
from django.core.exceptions import PermissionDenied

def my_view(request):
    if not user.is_authenticated:
        raise PermissionDenied("Login required")
```

## Examples

```python
# Example 1: Permission required
@login_required
@permission_required('blog.change_post', raise_exception=True)
def edit_post(request, pk):
    ...

# Example 2: Object-level permission
if request.user != post.author:
    raise PermissionDenied("Not your post")
```

## Related Errors

- [Django Settings Error]({{< relref "/frameworks/django/django-settings-error" >}}) — ImproperlyConfigured
- [Django CSRF Error]({{< relref "/frameworks/django/django-csrf-error" >}}) — CSRF verification failed
