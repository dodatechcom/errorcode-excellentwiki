---
title: "[Solution] TiDB Follower Read Error"
description: "How to fix TiDB follower read errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Follower not available
- Follower read not enabled
- Follower lag too high

## How to Fix

```sql
SET SESSION tidb_read_staleness = '-5s';
```

## Examples

```sql
SELECT * FROM mytable;
```
