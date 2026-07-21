---
title: "[Solution] TimescaleDB Access Node Query Error"
description: "How to fix TimescaleDB access node query errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query not routed to data node
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
