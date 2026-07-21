---
title: "[Solution] Rails Database Router Error"
description: "Database router not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Database router not working.

## Common Causes

Wrong router config.

## How to Fix

Configure router.

## Example

```ruby
class primary_only
  def reads; { database: :primary } end
  def writes; { database: :primary } end
end
```
