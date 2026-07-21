---
title: "[Solution] Rails Counter Cache Error"
description: "Counter showing wrong counts."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Counter showing wrong counts.

## Common Causes

Not configured.

## How to Fix

Add counter_cache.

## Example

```ruby
class Post < ApplicationRecord
  belongs_to :user, counter_cache: true
end
```
