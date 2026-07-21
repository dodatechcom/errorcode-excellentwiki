---
title: "[Solution] Rails Migration Version Error"
description: "Migration version wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration version wrong.

## Common Causes

Wrong class version.

## How to Fix

Use correct version.

## Example

```ruby
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :name
    end
  end
end
```
