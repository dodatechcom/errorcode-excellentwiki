---
title: "[Solution] Rails Scope Error"
description: "Scope returns wrong results."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Scope returns wrong results.

## Common Causes

Wrong scope syntax.

## How to Fix

Use lambda.

## Example

```ruby
class Post < ApplicationRecord
  scope :published, -> { where(published: true) }
end
```
