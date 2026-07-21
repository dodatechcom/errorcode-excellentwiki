---
title: "[Solution] Rails After Commit Error"
description: "after_commit not firing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

after_commit not firing.

## Common Causes

Wrong callback.

## How to Fix

Use after_commit.

## Example

```ruby
after_commit :do_something, on: [:create, :update]
```
