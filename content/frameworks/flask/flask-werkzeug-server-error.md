---
title: "[Solution] Flask Werkzeug Server Error"
description: "Dev server not starting."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Dev server not starting.

## Common Causes

Port in use.

## How to Fix

Use different port.

## Example

```python
app.run(host='0.0.0.0', port=5001)
```
