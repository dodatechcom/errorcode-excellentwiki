---
title: "[Solution] Flask Flask Blueprints Error"
description: "Blueprint URL prefix not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Blueprint URL prefix not working.

## Common Causes

Wrong prefix.

## How to Fix

Set prefix.

## Example

```python
api = Blueprint('api', __name__, url_prefix='/api')
```
