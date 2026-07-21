---
title: "[Solution] Rails Migration Change Error"
description: "change method not reversible."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

change method not reversible.

## Common Causes

Non-reversible operation.

## How to Fix

Use up/down.

## Example

```ruby
class My < ActiveRecord::Migration[7.0]
  def change
    reversible do |dir|
      dir.up { add_column :t, :c, :string }
      dir.down { remove_column :t, :c }
    end
  end
end
```
