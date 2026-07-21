---
title: "[Solution] Rails Model Touch Error"
description: "touch not updating timestamp."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

touch not updating timestamp.

## Common Causes

Wrong usage.

## How to Fix

Use touch.

## Example

```ruby
user.touch
user.touch(:last_seen_at)
```
