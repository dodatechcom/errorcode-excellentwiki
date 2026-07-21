---
title: "[Solution] Flask Flask Mail Send Error"
description: "Email send failing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Email send failing.

## Common Causes

SMTP unreachable.

## How to Fix

Check settings.

## Example

```python
from flask_mail import Mail, Message
msg = Message('Hi', recipients=['u@e.com'])
mail.send(msg)
```
