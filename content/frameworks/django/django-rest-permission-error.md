---
title: "[Solution] Django REST Permission Error"
description: "Permission class not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Permission class not working.

## Common Causes

Wrong class.

## How to Fix

Use correct class.

## Example

```python
from rest_framework.permissions import IsAuthenticated
class V(APIView):
    permission_classes = [IsAuthenticated]
```
