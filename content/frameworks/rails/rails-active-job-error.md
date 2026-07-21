---
title: "[Solution] Rails Active Job Error"
description: "Job not executing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Job not executing.

## Common Causes

Wrong adapter.

## How to Fix

Configure adapter.

## Example

```ruby
class WelcomeJob < ApplicationJob
  queue_as :default
  def perform(user)
    UserMailer.welcome(user).deliver_now
  end
end
```
