---
title: "[Solution] Rails Callback Order Error"
description: "Callback order wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Callback order wrong.

## Common Causes

Callbacks in wrong order.

## How to Fix

Order matters.

## Example

```ruby
before_validation :set_defaults
before_save :log_change
```
