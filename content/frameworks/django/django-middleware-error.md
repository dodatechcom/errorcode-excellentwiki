---
title: "[Solution] Django Middleware Processing Error — How to Fix"
description: "Fix Django middleware errors. Resolve middleware ordering, processing failures, and response handling issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django middleware processing error occurs when custom or third-party middleware fails during request or response processing. Middleware runs in a specific order, and errors in one middleware can cascade to affect the entire request cycle.

## Why It Happens

Django middleware processes every request and response in order. Errors occur when middleware raises exceptions during `__call__`, `process_view`, `process_exception`, or `process_response`, when middleware ordering is incorrect, when middleware references undefined variables, or when middleware doesn't properly call `get_response`. It's common with custom middleware and third-party packages.

## Common Error Messages

```
AttributeError: 'MyMiddleware' object has no attribute 'get_response'
```

```
TypeError: __init__() missing 1 required positional argument: 'get_response'
```

```
MiddlewareNotUsed: MyMiddleware is not in MIDDLEWARE
```

```
ImportError: cannot import name 'CustomMiddleware' from 'myapp.middleware'
```

## How to Fix It

### 1. Implement Middleware Correctly

Follow Django's middleware pattern with proper `__init__` and `__call__`:

```python
# myapp/middleware.py
import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start_time = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        duration = time.time() - start_time
        logger.info(f"Request to {request.path} took {duration:.3f}s")

        response['X-Request-Duration'] = f"{duration:.3f}s"
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Called just before Django calls the view.
        pass

    def process_exception(self, request, exception):
        # Called when a view raises an exception.
        logger.error(f"Exception in {request.path}: {exception}")
        return None  # Let Django handle the exception

    def process_template_response(self, request, response):
        # Called after the view has finished executing.
        return response
```

### 2. Configure Middleware Order Correctly

Order matters — security middleware first, common middleware last:

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # First
    'django.contrib.sessions.middleware.SessionMiddleware',    # Before CSRF
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',              # After session
    'django.contrib.auth.middleware.AuthenticationMiddleware', # After session
    'django.contrib.messages.middleware.MessageMiddleware',    # After auth
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom middleware (usually after built-in)
    'myapp.middleware.RequestTimingMiddleware',
    'myapp.middleware.APILoggingMiddleware',
]
```

### 3. Handle Exceptions Gracefully

Prevent middleware exceptions from crashing the application:

```python
class SafeErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            logger.error(f"Middleware error: {e}")
            # Return a basic error response instead of crashing
            from django.http import HttpResponseServerError
            return HttpResponseServerError("Internal server error")
```

### 4. Use process_view for View-Level Checks

Run middleware logic that needs access to the resolved view:

```python
class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limiter = RateLimiter()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check rate limit before the view executes
        if self.rate_limiter.is_rate_limited(request):
            from django.http import JsonResponse
            return JsonResponse(
                {'error': 'Rate limit exceeded'},
                status=429
            )
        return None  # Continue to the view
```

## Common Scenarios

**Scenario 1: Middleware causes circular import.**
If middleware imports from a module that also imports the middleware, you get a circular import. Use string-based middleware references in `MIDDLEWARE` or defer imports to inside the `__call__` method.

**Scenario 2: Middleware doesn't call get_response.**
If `__call__` doesn't call `self.get_response(request)`, the request will never reach the view or subsequent middleware. Always ensure `get_response` is called unless you intentionally want to short-circuit.

**Scenario 3: Middleware runs on every request including admin.**
If your middleware adds overhead to admin pages, use request path checks to skip processing for certain URLs:

```python
def __call__(self, request):
    if request.path.startswith('/admin/'):
        return self.get_response(request)
    # Apply middleware logic for non-admin paths
    # ...
```

## Prevent It

1. **Write tests for middleware.** Test both request and response processing, and verify middleware order by checking the response chain.

2. **Keep middleware lightweight.** Middleware runs on every request. Avoid expensive operations like database queries unless absolutely necessary.

3. **Use `MiddlewareMixin` for compatibility** when migrating from old-style middleware to the new format.
