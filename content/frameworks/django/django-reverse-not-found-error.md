---
title: "[Solution] Django Reverse Not Found Error"
description: "reverse() failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

reverse() failing.

## Common Causes

Wrong args.

## How to Fix

Check URL config.

## Example

```python
from django.urls import reverse
url = reverse('user-detail', kwargs={'pk': u.pk})
```
