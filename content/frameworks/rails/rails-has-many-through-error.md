---
title: "[Solution] Rails Has Many Through Error"
description: "Through association not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Through association not working.

## Common Causes

Wrong through setup.

## How to Fix

Configure correctly.

## Example

```ruby
class Doctor < ApplicationRecord
  has_many :appointments
  has_many :patients, through: :appointments
end
```
