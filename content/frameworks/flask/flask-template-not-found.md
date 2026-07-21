---
title: "[Solution] Flask Template Not Found"
description: "Jinja2 template missing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Jinja2 template missing.

## Common Causes

Wrong name.

## How to Fix

Check templates/.

## Example

```python
return render_template('index.html')
```
