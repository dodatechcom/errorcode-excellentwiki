---
title: "[Solution] Rails Database Connection Pool Error"
description: "Connection pool exhausted."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Connection pool exhausted.

## Common Causes

Pool too small.

## How to Fix

Increase pool.

## Example

```yaml
development:
  pool: 10
```
