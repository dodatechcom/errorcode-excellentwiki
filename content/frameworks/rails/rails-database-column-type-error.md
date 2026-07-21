---
title: "[Solution] Rails Database Column Type Error"
description: "Column type wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Column type wrong.

## Common Causes

Wrong type specified.

## How to Fix

Use correct type.

## Example

```ruby
add_column :users, :price, :decimal, precision: 10, scale: 2
```
