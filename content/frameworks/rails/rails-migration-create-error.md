---
title: "[Solution] Rails Migration Create Error"
description: "Create table failing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Create table failing.

## Common Causes

Wrong syntax.

## How to Fix

Use create_table.

## Example

```ruby
class Create < ActiveRecord::Migration[7.0]
  def change
    create_table :items do |t|
      t.string :name
      t.timestamps
    end
  end
end
```
