---
title: "[Solution] Rails Validation Failed Error"
description: "RecordInvalid raised."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

RecordInvalid raised.

## Common Causes

Record fails validations.

## How to Fix

Check validations.

## Example

```ruby
class User < ApplicationRecord
  validates :email, presence: true
end
```
