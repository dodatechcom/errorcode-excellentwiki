---
title: "[Solution] Django Template Context Error Django"
description: "Template variable undefined."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Template variable undefined.

## Common Causes

Variable not passed.

## How to Fix

Pass in context.

## Example

```python
return render(request, 'page.html', {'title': 'Hello'})
```
