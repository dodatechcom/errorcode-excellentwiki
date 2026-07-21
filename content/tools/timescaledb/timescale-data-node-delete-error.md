---
title: "[Solution] TimescaleDB Data Node Delete Error"
description: "How to fix TimescaleDB data node delete errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Data node still attached
- Data node has data
- Delete while query running

## How to Fix

```sql
SELECT delete_data_node('data_node_1', force => true);
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
