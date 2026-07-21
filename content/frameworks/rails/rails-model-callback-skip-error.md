---
title: "[Solution] Rails Model Callback Skip Error"
description: "Skip callback not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Skip callback not working.

## Common Causes

Wrong method.

## How to Fix

Use skip_callback.

## Example

```ruby
User.skip_callback(:save, :before, :my_callback)
```
