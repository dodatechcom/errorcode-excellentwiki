---
title: "[Solution] Django ManyToMany Error"
description: "ManyToMany not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

ManyToMany not working.

## Common Causes

Wrong definition.

## How to Fix

Define correctly.

## Example

```python
class Post(models.Model):
    tags = models.ManyToManyField(Tag)
```
