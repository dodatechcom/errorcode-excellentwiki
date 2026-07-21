---
title: "[Solution] Rails Transaction Rollback Error"
description: "Transaction rolling back."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Transaction rolling back.

## Common Causes

Exception in block.

## How to Fix

Handle exceptions.

## Example

```ruby
ActiveRecord::Base.transaction do
  user.save!
rescue ActiveRecord::RecordInvalid => e
  # handle
end
```
