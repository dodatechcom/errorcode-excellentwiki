---
title: "[Solution] Django HttpResponseRedirect Error"
description: "HttpResponseRedirect not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

HttpResponseRedirect not working.

## Common Causes

Wrong usage.

## How to Fix

Use redirect.

## Example

```python
from django.http import HttpResponseRedirect
return HttpResponseRedirect('/new-url/')
```
