---
title: "[Solution] Rails Model Dirty Change Error"
description: "changes method wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

changes method wrong.

## Common Causes

Not using correct method.

## How to Fix

Use changes.

## Example

```ruby
user.name = 'New'
user.changes # => { 'name' => ['Old', 'New'] }
```
