---
title: "[Solution] Flask Flask RESTful Resource Error"
description: "Resource not responding."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Resource not responding.

## Common Causes

Wrong method.

## How to Fix

Define methods.

## Example

```python
from flask_restful import Resource
class U(Resource):
    def get(self, id): return {'u': id}
```
