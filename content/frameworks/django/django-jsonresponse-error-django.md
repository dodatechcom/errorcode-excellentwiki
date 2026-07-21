---
title: "[Solution] Django JsonResponse Error Django"
description: "JsonResponse failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

JsonResponse failing.

## Common Causes

Data not serializable.

## How to Fix

Ensure JSON safe.

## Example

```python
from django.http import JsonResponse
return JsonResponse({'d': 'ok'})
```
