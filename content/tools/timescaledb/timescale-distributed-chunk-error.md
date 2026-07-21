---
title: "[Solution] TimescaleDB Distributed Chunk Error"
description: "How to fix TimescaleDB distributed chunk errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Chunk not placed on data node
- Chunk placement failed
- Data node unreachable

## How to Fix

```sql
SELECT * FROM timescaledb_information.chunks WHERE hypertable_name = 'conditions';
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
