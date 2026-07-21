---
title: "[Solution] Rails Migration Index Error"
description: "Migration index wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration index wrong.

## Common Causes

Duplicate index.

## How to Fix

Check existing indexes.

## Example

```ruby
class AddIndex < ActiveRecord::Migration[7.0]
  def change
    add_index :users, :email, unique: true
  end
end
```
