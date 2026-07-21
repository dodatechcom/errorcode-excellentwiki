---
title: "[Solution] Rails Transaction Deadlock Error"
description: "Transaction deadlock."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Transaction deadlock.

## Common Causes

Multiple locks.

## How to Fix

Retry on deadlock.

## Example

```ruby
retry_on ActiveRecord::Deadlocked, wait: 1.second, attempts: 3
```
