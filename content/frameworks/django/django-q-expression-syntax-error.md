---
title: "[Solution] Django Q Expression Syntax Error"
description: "Q expression syntax wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Q expression syntax wrong.

## Common Causes

Wrong operator.

## How to Fix

Use & | ~.

## Example

```python
User.objects.filter(Q(name='J') & Q(active=True))
```
