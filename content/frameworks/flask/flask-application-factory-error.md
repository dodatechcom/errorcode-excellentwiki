---
title: "[Solution] Flask Application Factory Error"
description: "create_app not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

create_app not working.

## Common Causes

Wrong structure.

## How to Fix

Return app.

## Example

```python
def create_app():
    app = Flask(__name__)
    return app
```
