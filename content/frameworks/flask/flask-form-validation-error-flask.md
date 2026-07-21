---
title: "[Solution] Flask Form Validation Error Flask"
description: "Validation not running."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Validation not running.

## Common Causes

No validators.

## How to Fix

Add validators.

## Example

```python
from wtforms.validators import DataRequired
class F(FlaskForm):
    email = StringField(validators=[DataRequired()])
```
