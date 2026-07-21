---
title: "[Solution] Django Form is_valid Error"
description: "Validation not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Validation not working.

## Common Causes

No validators.

## How to Fix

Add validators.

## Example

```python
if form.is_valid(): d = form.cleaned_data
```
