---
title: "[Solution] Rails Scope Error Query"
description: "Scope query wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Scope query wrong.

## Common Causes

Wrong query syntax.

## How to Fix

Use correct syntax.

## Example

```ruby
scope :active, -> { where(active: true) }
scope :recent, ->(days) { where('created_at > ?', days.days.ago) }
```
