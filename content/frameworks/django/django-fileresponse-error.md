---
title: "[Solution] Django FileResponse Error"
description: "FileResponse not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

FileResponse not working.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
from django.http import FileResponse
return FileResponse(open('file.pdf', 'rb'))
```
