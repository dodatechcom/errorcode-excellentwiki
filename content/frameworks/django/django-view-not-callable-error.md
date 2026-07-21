---
title: "[Solution] Django View Not Callable Error"
description: "View not callable."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

View not callable.

## Common Causes

Not a function.

## How to Fix

Ensure callable.

## Example

```python
def my_view(request): return HttpResponse('Hi')
```
