---
title: "[Solution] Rails Lock Version Error"
description: "Lock version column missing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Lock version column missing.

## Common Causes

Column not added.

## How to Fix

Add column.

## Example

```ruby
class AddLockVersion < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :lock_version, :integer, default: 0, null: false
  end
end
```
