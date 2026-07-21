---
title: "[Solution] Rails Active Job Perform Error"
description: "perform method wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

perform method wrong.

## Common Causes

Wrong arguments.

## How to Fix

Match arguments.

## Example

```ruby
def perform(user_id)
  user = User.find(user_id)
  UserMailer.welcome(user).deliver_now
end
```
