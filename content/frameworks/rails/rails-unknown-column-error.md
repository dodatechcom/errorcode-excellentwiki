---
title: "[Solution] Rails Unknown Column Error"
description: "Column does not exist."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Column does not exist.

## Common Causes

Column not in schema.

## How to Fix

Add column via migration.

## Example

```ruby
class AddEmail < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :email, :string
  end
end
```
