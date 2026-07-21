---
title: "[Solution] Rails Dependent Destroy Error"
description: "Records not deleted."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Records not deleted.

## Common Causes

Missing dependent option.

## How to Fix

Add dependent: :destroy.

## Example

```ruby
class User < ApplicationRecord
  has_many :posts, dependent: :destroy
end
```
