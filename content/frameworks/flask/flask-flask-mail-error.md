---
title: "[Solution] Flask Flask-Mail Error"
description: "Email not sent."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Email not sent.

## Common Causes

Wrong SMTP.

## How to Fix

Configure mail.

## Example

```python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
```
