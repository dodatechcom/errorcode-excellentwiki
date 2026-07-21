---
title: "[Solution] Rails Model Store Accessor Error"
description: "Store accessor not persisting."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Store accessor not persisting.

## Common Causes

Wrong column type.

## How to Fix

Use json/jsonb.

## Example

```ruby
store_accessor :preferences, :theme, :notifications
```
