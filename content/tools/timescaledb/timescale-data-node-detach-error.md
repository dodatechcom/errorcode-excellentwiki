---
title: "[Solution] TimescaleDB Data Node Detach Error"
description: "How to fix TimescaleDB data node detach errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Data node not attached
- Data node still has data
- Detach while query running

## How to Fix

```sql
SELECT detach_data_node('data_node_1', 'conditions', force => true);
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
