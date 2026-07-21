---
title: "[Solution] Rails Model Scope Error"
description: "Scope returning wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Scope returning wrong.

## Common Causes

Wrong scope definition.

## How to Fix

Define correctly.

## Example

```ruby
scope :for_role, ->(role) { where(role: role) }
```
