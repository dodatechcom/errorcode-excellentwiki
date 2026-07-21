---
title: "[Solution] Rails Migration Rename Error"
description: "Migration rename wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration rename wrong.

## Common Causes

Column not renamed.

## How to Fix

Use rename_column.

## Example

```ruby
class Rename < ActiveRecord::Migration[7.0]
  def change
    rename_column :users, :name, :full_name
  end
end
```
