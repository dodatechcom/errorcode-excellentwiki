---
title: "[Solution] Rails Default Scope Override Error"
description: "Cannot override default scope."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot override default scope.

## Common Causes

Using unscoped.

## How to Fix

Use unscope.

## Example

```ruby
Post.unscoped.where(published: true)
```
