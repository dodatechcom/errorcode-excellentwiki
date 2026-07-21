---
title: "[Solution] Flask Config From File Error"
description: "Config not loading from file."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Config not loading from file.

## Common Causes

Wrong path.

## How to Fix

Load from file.

## Example

```python
app.config.from_pyinstance('config.py')
```
