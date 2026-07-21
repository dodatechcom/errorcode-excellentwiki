---
title: "[Solution] Rails Action Text Error"
description: "Rich text not rendering."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Rich text not rendering.

## Common Causes

Migration not run.

## How to Fix

Run migrations.

## Example

```ruby
class Post < ApplicationRecord
  has_rich_text :body
end
```
