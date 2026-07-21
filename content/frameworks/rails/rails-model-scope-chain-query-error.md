---
title: "[Solution] Rails Model Scope Chain Query Error"
description: "Chained scopes returning wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Chained scopes returning wrong.

## Common Causes

Scope composition issue.

## How to Fix

Chain correctly.

## Example

```ruby
User.active.recent.for_role('admin')
```
