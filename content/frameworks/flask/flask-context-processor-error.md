---
title: "[Solution] Flask Context Processor Error"
description: "Context processor not providing vars."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Context processor not providing vars.

## Common Causes

Not returning dict.

## How to Fix

Return dict.

## Example

```python
@app.context_processor
def inject(): return dict(user=get_user())
```
