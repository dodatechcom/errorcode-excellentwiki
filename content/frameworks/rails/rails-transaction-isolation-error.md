---
title: "[Solution] Rails Transaction Isolation Error"
description: "Wrong isolation level."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Wrong isolation level.

## Common Causes

Not configured.

## How to Fix

Set isolation.

## Example

```ruby
ActiveRecord::Base.transaction(isolation: :serializable) { ... }
```
