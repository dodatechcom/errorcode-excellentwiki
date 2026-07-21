---
title: "[Solution] Rails Unicorn Worker Error"
description: "Unicorn workers timing out."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Unicorn workers timing out.

## Common Causes

Timeout too short.

## How to Fix

Adjust timeout.

## Example

```ruby
timeout 30
preload_app true
```
