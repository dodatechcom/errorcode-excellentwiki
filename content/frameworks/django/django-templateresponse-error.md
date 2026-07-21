---
title: "[Solution] Django TemplateResponse Error"
description: "TemplateResponse not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

TemplateResponse not working.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
from django.template.response import TemplateResponse
return TemplateResponse(request, 'page.html', {'d': data})
```
