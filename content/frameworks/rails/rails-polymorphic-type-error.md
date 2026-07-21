---
title: "[Solution] Rails Polymorphic Type Error"
description: "Polymorphic association wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Polymorphic association wrong.

## Common Causes

Type column missing.

## How to Fix

Add type column.

## Example

```ruby
class Comment < ApplicationRecord
  belongs_to :commentable, polymorphic: true
end
```
