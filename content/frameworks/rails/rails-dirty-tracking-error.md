---
title: "[Solution] Rails Dirty Tracking Error"
description: "Changes not detected."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Changes not detected.

## Common Causes

Using update_columns.

## How to Fix

Use standard assignment.

## Example

```ruby
u.name = 'New'
u.name_changed? # true
```
