---
title: "[Solution] Rails Belongs To Required Error"
description: "RecordInvalid for missing association."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

RecordInvalid for missing association.

## Common Causes

belongs_to required.

## How to Fix

Use optional: true.

## Example

```ruby
class Comment < ApplicationRecord
  belongs_to :post, optional: true
end
```
