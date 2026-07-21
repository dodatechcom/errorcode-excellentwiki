---
title: "[Solution] Rails Enum Conflict Error"
description: "Enum value conflicts."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Enum value conflicts.

## Common Causes

Reserved word used.

## How to Fix

Use different name.

## Example

```ruby
enum status: { open: 0, closed: 1 }, _prefix: true
```
