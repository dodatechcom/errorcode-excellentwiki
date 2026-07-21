---
title: "[Solution] Django Model Form Error"
description: "ModelForm not rendering."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

ModelForm not rendering.

## Common Causes

Wrong fields.

## How to Fix

Define fields.

## Example

```python
class UF(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
```
