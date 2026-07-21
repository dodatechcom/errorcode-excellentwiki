---
title: "[Solution] Rails Model Include Error"
description: "Module include wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Module include wrong.

## Common Causes

Not including module.

## How to Fix

Include module.

## Example

```ruby
class User < ApplicationRecord
  include SoftDeletable
end
```
