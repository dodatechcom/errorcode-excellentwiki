---
title: "[Solution] Django Template Filter Register Error"
description: "Template filter not registered."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Template filter not registered.

## Common Causes

Not registered.

## How to Fix

Register filter.

## Example

```python
from django import template
register = template.Library()
@register.filter
def my_filter(value): return value.upper()
```
