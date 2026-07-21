---
title: "[Solution] Rails Scope Chain Error"
description: "Scope chain not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Scope chain not working.

## Common Causes

Wrong chaining.

## How to Fix

Chain scopes.

## Example

```ruby
Post.published.recent.where(author: user)
```
