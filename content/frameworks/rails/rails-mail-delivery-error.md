---
title: "[Solution] Rails Mail Delivery Error"
description: "Email not sent."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Email not sent.

## Common Causes

Wrong SMTP.

## How to Fix

Configure mail.

## Example

```ruby
config.action_mailer.delivery_method = :smtp
```
