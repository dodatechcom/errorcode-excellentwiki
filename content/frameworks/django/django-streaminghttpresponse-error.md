---
title: "[Solution] Django StreamingHttpResponse Error"
description: "StreamingResponse not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

StreamingResponse not working.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
from django.http import StreamingHttpResponse
def generate(): yield 'line 1\n'
return StreamingHttpResponse(generate())
```
