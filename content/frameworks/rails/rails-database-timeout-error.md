---
title: "[Solution] Rails Database Timeout Error"
description: "Database timeout."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Database timeout.

## Common Causes

Query too slow.

## How to Fix

Add timeout.

## Example

```yaml
development:
  timeout: 5000
```
