---
title: "[Solution] Rails Polymorphic Association Error"
description: "Polymorphic query wrong."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Polymorphic query wrong.

## Common Causes

Wrong syntax.

## How to Fix

Use correct syntax.

## Example

```ruby
Comment.where(commentable_type: 'Post', commentable_id: 1)
```
