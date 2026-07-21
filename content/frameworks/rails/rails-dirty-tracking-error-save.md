---
title: "[Solution] Rails Dirty Tracking Error Save"
description: "Changes not saved."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Changes not saved.

## Common Causes

Not using save.

## How to Fix

Use save after changes.

## Example

```ruby
user.name = 'New'
save
```
