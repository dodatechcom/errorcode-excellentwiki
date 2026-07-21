---
title: "[Solution] Flask Flask-WTF Error"
description: "WTForms not rendering."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

WTForms not rendering.

## Common Causes

Form not defined.

## How to Fix

Define form.

## Example

```python
from flask_wtf import FlaskForm
class F(FlaskForm):
    name = StringField('Name')
```
