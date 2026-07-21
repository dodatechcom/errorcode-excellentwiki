---
title: "[Solution] Rails Counter Cache Reset Error"
description: "Counter cache wrong count."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Counter cache wrong count.

## Common Causes

Not reset.

## How to Fix

Reset counters.

## Example

```ruby
User.find_each { |u| User.reset_counters(u.id, :posts) }
```
