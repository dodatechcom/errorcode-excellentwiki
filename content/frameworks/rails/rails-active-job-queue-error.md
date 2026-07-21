---
title: "[Solution] Rails Active Job Queue Error"
description: "Job on wrong queue."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Job on wrong queue.

## Common Causes

Queue not configured.

## How to Fix

Set queue.

## Example

```ruby
queue_as :critical
```
