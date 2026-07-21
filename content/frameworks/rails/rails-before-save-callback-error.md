---
title: "[Solution] Rails Before Save Callback Error"
description: "Save prevented."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Save prevented.

## Common Causes

Callback returning false.

## How to Fix

Return true.

## Example

```ruby
before_save :set_defaults
```
