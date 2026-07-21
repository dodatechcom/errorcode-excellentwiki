---
title: "[Solution] Django Model MultipleObjectsReturned Error"
description: "MultipleObjectsReturned."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

MultipleObjectsReturned.

## Common Causes

Expected one, got multiple.

## How to Fix

Use filter or first.

## Example

```python
user = User.objects.filter(name='John').first()
```
