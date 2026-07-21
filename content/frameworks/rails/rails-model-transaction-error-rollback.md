---
title: "[Solution] Rails Model Transaction Error Rollback"
description: "Transaction rollback not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Transaction rollback not working.

## Common Causes

Not catching.

## How to Fix

Rescue exception.

## Example

```ruby
begin
  ActiveRecord::Base.transaction { ... }
rescue ActiveRecord::RecordInvalid
  # handle
end
```
