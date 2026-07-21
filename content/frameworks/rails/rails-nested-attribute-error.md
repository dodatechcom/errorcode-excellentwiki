---
title: "[Solution] Rails Nested Attribute Error"
description: "Nested attributes not saving."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Nested attributes not saving.

## Common Causes

Not accepting.

## How to Fix

Use accepts_nested_attributes_for.

## Example

```ruby
class User < ApplicationRecord
  has_many :posts
  accepts_nested_attributes_for :posts, allow_destroy: true
end
```
