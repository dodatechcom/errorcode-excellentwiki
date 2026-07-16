---
title: "View function error"
description: "Django view function raises an unhandled exception during request processing"
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["views", "request", "exception", "http"]
weight: 5
---

This error occurs when a Django view function raises an unhandled exception. In production, this results in a 500 error page. In development, Django's debug view shows the full traceback.

## Common Causes

- Uncaught exceptions from database queries (e.g. DoesNotExist)
- Missing required parameters in the view signature
- Returning a non-Response object
- Improperly handling request.POST or request.GET data

## How to Fix

1. Handle exceptions explicitly in views:

```python
from django.http import Http404

def detail(request, pk):
    try:
        obj = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        raise Http404("Object not found")
    return render(request, "detail.html", {"object": obj})
```

2. Use exception handling middleware:

```python
class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        logger.error(f"Error: {exception}", exc_info=True)
        return None
```

3. Always return an HttpResponse subclass:

```python
def my_view(request):
    return render(request, "page.html", {"data": data})
```

## Examples

```python
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)  # raises User.DoesNotExist
    return render(request, "user.html", {"user": user})
```

```text
django.core.exceptions.ObjectDoesNotExist: User matching query does not exist.
```

## Related Errors

- [Migration error]({{< relref "/frameworks/django/migration-error" >}})
