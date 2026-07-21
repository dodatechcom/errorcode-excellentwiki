---
title: "[Solution] Django Related Object Error Django"
description: "Related object not accessible."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Related object not accessible.

## Common Causes

Wrong related_name.

## How to Fix

Check related_name.

## Example

```python
user.posts.all()  # reverse relation
```
