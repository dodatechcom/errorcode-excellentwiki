---
title: "[Solution] Flask Flask JSON Response Error"
description: "jsonify not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

jsonify not working.

## Common Causes

Wrong data.

## How to Fix

Use jsonify.

## Example

```python
from flask import jsonify
return jsonify({'key': 'value'})
```
