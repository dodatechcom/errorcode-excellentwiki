---
title: "[Solution] Rails Join Table Missing Error"
description: "Join table does not exist."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Join table does not exist.

## Common Causes

Migration missing.

## How to Fix

Create join table.

## Example

```ruby
class CreateJoinTable < ActiveRecord::Migration[7.0]
  def change
    create_join_table :users, :roles
  end
end
```
