---
title: "[Solution] Rails Model Callback Error"
description: "Callback throwing exception."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Callback throwing exception.

## Common Causes

Not handling.

## How to Fix

Use begin/rescue.

## Example

```ruby
after_create :do_something
```
