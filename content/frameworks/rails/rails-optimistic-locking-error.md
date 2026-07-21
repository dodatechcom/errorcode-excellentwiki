---
title: "[Solution] Rails Optimistic Locking Error"
description: "Stale object error."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Stale object error.

## Common Causes

Concurrent update.

## How to Fix

Handle error.

## Example

```ruby
class User < ApplicationRecord
  self.locking_column = :lock_version
end
```
