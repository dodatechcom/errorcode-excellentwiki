---
title: "[Solution] Rails Relation Error"
description: "Relation not returning."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Relation not returning.

## Common Causes

Wrong query.

## How to Fix

Check relation.

## Example

```ruby
User.where(active: true).order(:name)
```
