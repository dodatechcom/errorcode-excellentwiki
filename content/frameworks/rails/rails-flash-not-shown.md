---
title: "[Solution] Rails Flash Not Shown"
description: "Flash not displaying."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Flash not displaying.

## Common Causes

Using flash with render.

## How to Fix

Use flash.now.

## Example

```ruby
flash.now[:notice] = 'Saved!'
render :new
```
