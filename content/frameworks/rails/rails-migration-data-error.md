---
title: "[Solution] Rails Migration Data Error"
description: "Migration data loss."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration data loss.

## Common Causes

Not reversible.

## How to Fix

Use reversible.

## Example

```ruby
class FixData < ActiveRecord::Migration[7.0]
  def up
    execute "UPDATE users SET role = 'user' WHERE role IS NULL"
  end
  def down
    execute "UPDATE users SET role = NULL WHERE role = 'user'"
  end
end
```
