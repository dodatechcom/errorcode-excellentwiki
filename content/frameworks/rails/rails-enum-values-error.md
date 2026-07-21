---
title: "[Solution] Rails Enum Values Error"
description: "Enum mapping wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Enum mapping wrong.

## Common Causes

Definition mismatch.

## How to Fix

Define enums correctly.

## Example

```ruby
class Order < ApplicationRecord
  enum status: { pending: 0, shipped: 1 }
end
```
