---
title: "[Solution] Rails Migration Column Rename Error"
description: "Column rename not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Column rename not working.

## Common Causes

Wrong syntax.

## How to Fix

Use rename_column.

## Example

```ruby
class Rename < ActiveRecord::Migration[7.0]
  def change
    rename_column :users, :old_name, :new_name
  end
end
```
