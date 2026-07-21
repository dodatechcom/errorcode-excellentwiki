---
title: "[Solution] ScyllaDB Consistency Level Error"
description: "How to fix ScyllaDB consistency level errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Not enough replicas for requested consistency
- Consistency level too high for current topology
- Network partition preventing quorum

## How to Fix

Use appropriate consistency:

```cql
CONSISTENCY ONE;  -- Lowest consistency
CONSISTENCY QUORUM;  -- Majority
CONSISTENCY ALL;  -- All replicas
```

Reduce consistency temporarily:

```cql
CONSISTENCY ONE;
INSERT INTO my_table (id, val) VALUES (1, 'a');
```

## Examples

```cql
CONSISTENCY;
CONSISTENCY QUORUM;
SELECT * FROM my_table WHERE id = 1;
```
