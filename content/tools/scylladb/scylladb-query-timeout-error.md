---
title: "[Solution] ScyllaDB Query Timeout Error"
description: "How to fix ScyllaDB query timeout errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query too slow
- Network latency high
- Too many tombstones scanned

## How to Fix

```cql
SELECT * FROM mytable WHERE id = 1 USING TIMEOUT 5s;
```

## Examples

```cql
SELECT * FROM mytable WHERE id = 1 CONSISTENCY ONE;
```
