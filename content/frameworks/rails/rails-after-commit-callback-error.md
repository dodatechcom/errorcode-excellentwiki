---
title: "[Solution] Rails After Commit Callback Error"
description: "Callback not firing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Callback not firing.

## Common Causes

Not defined.

## How to Fix

Use after_commit.

## Example

```ruby
class User < ApplicationRecord
  after_commit :notify, on: :create
end
```
