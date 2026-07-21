---
title: "[Solution] Flask Flask Redirect URL Error"
description: "Redirect to wrong URL."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Redirect to wrong URL.

## Common Causes

Wrong endpoint.

## How to Fix

Use url_for.

## Example

```python
return redirect(url_for('login'))
```
