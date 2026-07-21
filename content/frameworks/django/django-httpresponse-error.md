---
title: "[Solution] Django HttpResponse Error"
description: "HttpResponse wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

HttpResponse wrong.

## Common Causes

Wrong return.

## How to Fix

Return HttpResponse.

## Example

```python
from django.http import HttpResponse
return HttpResponse('Hello')
```
