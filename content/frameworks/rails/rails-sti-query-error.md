---
title: "[Solution] Rails STI Query Error"
description: "STI query not filtering."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

STI query not filtering.

## Common Causes

Missing type condition.

## How to Fix

Query with type.

## Example

```ruby
Dog.where(type: 'Dog')
```
