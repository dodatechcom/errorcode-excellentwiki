---
title: "[Solution] Django Model Save Update Error"
description: "save() not updating."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

save() not updating.

## Common Causes

Using create instead.

## How to Fix

Use update or save.

## Example

```python
user.name = 'New'
user.save()
```
