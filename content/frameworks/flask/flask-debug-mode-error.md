---
title: "[Solution] Flask Debug Mode Error"
description: "Debug exposing info."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Debug exposing info.

## Common Causes

DEBUG=True.

## How to Fix

Set False in prod.

## Example

```python
app.run(debug=False)
```
