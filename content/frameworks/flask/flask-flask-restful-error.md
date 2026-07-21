---
title: "[Solution] Flask Flask-RESTful Error"
description: "API resource not responding."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

API resource not responding.

## Common Causes

Wrong method.

## How to Fix

Define correctly.

## Example

```python
from flask_restful import Resource, Api
class U(Resource):
    def get(self, id): return {'u': id}
api.add_resource(U, '/u/<int:id>')
```
