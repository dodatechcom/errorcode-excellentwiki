---
title: "[Solution] ScyllaDB Read Repair Error"
description: "How to fix ScyllaDB read repair errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Read repair too aggressive
- Consistency level mismatch
- Hinted handoff not working

## How to Fix

```yaml
read_repair_chance: 0.0
dclocal_read_repair_chance: 0.0
```

## Examples

```cql
SELECT * FROM mytable WHERE id = 1 CONSISTENCY LOCAL_QUORUM;
```
