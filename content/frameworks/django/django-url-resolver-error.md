---
title: "[Solution] Django URL Resolver Error"
description: "URL resolver not matching."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

URL resolver not matching.

## Common Causes

Wrong pattern.

## How to Fix

Check patterns.

## Example

```python
urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
]
```
