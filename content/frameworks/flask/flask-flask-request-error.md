---
title: "[Solution] Flask Flask Request Error"
description: "Request data not accessible."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Request data not accessible.

## Common Causes

Wrong content type.

## How to Fix

Check request content type.

## Example

```python
if request.is_json:
    data = request.get_json()
else:
    data = request.form
```
