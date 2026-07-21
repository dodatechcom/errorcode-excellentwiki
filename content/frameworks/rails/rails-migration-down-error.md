---
title: "[Solution] Rails Migration Down Error"
description: "Migration down not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration down not working.

## Common Causes

Wrong down method.

## How to Fix

Define down.

## Example

```ruby
class MyMigration < ActiveRecord::Migration[7.0]
  def up
    add_column :users, :bio, :text
  end
  def down
    remove_column :users, :bio
  end
end
```
