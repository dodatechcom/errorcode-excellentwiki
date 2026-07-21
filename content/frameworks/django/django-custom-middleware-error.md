---
title: "[Solution] Django Custom Middleware Error"
description: "Custom middleware not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom middleware not working.

## Common Causes

Wrong implementation.

## How to Fix

Implement correctly.

## Example

```python
class MyMiddleware:
    def __init__(self, get_response): self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response
```
