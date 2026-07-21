---
title: "[Solution] Rails Model Counter Cache Error"
description: "Counter cache not updating."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Counter cache not updating.

## Common Causes

Not using method.

## How to Fix

Use increment!

## Example

```ruby
user.increment!(:posts_count)
```
