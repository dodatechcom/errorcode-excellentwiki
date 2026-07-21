---
title: "[Solution] Rails Before Destroy Error"
description: "before_destroy preventing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

before_destroy preventing.

## Common Causes

Returning false.

## How to Fix

Use throw(:abort).

## Example

```ruby
before_destroy :check_dependencies
```
