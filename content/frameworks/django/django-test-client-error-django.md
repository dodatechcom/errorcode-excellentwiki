---
title: "[Solution] Django Test Client Error Django"
description: "Test client not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Test client not working.

## Common Causes

Wrong usage.

## How to Fix

Use client.

## Example

```python
response = self.client.get('/api/')
self.assertEqual(response.status_code, 200)
```
