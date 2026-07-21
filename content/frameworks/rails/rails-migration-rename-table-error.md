---
title: "[Solution] Rails Migration Rename Table Error"
description: "Table rename wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Table rename wrong.

## Common Causes

Not using rename.

## How to Fix

Use rename_table.

## Example

```ruby
class Rename < ActiveRecord::Migration[7.0]
  def change
    rename_table :users, :accounts
  end
end
```
