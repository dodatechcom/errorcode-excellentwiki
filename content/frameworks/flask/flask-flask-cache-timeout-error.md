---
title: "[Solution] Flask Flask Cache Timeout Error"
description: "Cache timeout wrong."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Cache timeout wrong.

## Common Causes

Wrong timeout.

## How to Fix

Set timeout.

## Example

```python
@cache.cached(timeout=300)
def get_data(): return expensive()
```
