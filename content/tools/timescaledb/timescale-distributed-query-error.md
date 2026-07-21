---
title: "[Solution] TimescaleDB Distributed Query Error"
description: "How to fix TimescaleDB distributed query errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query not reaching data node
- Data node unreachable
- Query timeout

## How to Fix

```sql
EXPLAIN SELECT * FROM conditions WHERE time > now() - INTERVAL '1 hour';
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
