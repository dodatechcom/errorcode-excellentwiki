---
title: "[Solution] Django Template Inclusion Tag Error"
description: "Inclusion tag not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Inclusion tag not working.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
@register.inclusion_tag('template.html')
def show_items(items): return {'items': items}
```
