---
title: "[Solution] Rails Model Transaction Error"
description: "Transaction not saving."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Transaction not saving.

## Common Causes

Exception in transaction.

## How to Fix

Handle exception.

## Example

```ruby
ActiveRecord::Base.transaction do
  user.save!
  post.save!
rescue => e
  Rails.logger.error e.message
end
```
