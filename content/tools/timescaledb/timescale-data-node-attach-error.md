---
title: "[Solution] TimescaleDB Data Node Attach Error"
description: "How to fix TimescaleDB data node attach errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Data node not found
- Data node already attached
- Schema not synced

## How to Fix

```sql
SELECT attach_data_node('data_node_1', 'conditions');
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
