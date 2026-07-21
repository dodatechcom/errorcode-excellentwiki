---
title: "[Solution] Flask Flask JSON Encoder Error"
description: "JSON encoder not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

JSON encoder not working.

## Common Causes

Wrong encoder.

## How to Fix

Customize encoder.

## Example

```python
import json
from flask.json.provider import DefaultJSONProvider
```
