---
title: "[Solution] Flask Template Filter Error"
description: "Custom filter not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom filter not working.

## Common Causes

Not registered.

## How to Fix

Register filter.

## Example

```python
@app.template_filter('dt')
def dt_filter(value, fmt='%Y-%m-%d'):
    return value.strftime(fmt)
```
