---
title: "[Solution] Rails Transaction Nested Error"
description: "Nested transaction not saving."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Nested transaction not saving.

## Common Causes

Using begin.

## How to Fix

Use savepoints.

## Example

```ruby
ActiveRecord::Base.transaction do
  User.transaction do
    user.save!
  end
end
```
