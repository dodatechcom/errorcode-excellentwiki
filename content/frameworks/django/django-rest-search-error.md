---
title: "[Solution] Django REST Search Error"
description: "Search not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Search not working.

## Common Causes

Not configured.

## How to Fix

Configure search.

## Example

```python
class V(viewSets.ModelViewSet):
    search_fields = ['name', 'email']
```
