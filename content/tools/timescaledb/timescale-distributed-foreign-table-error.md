---
title: "[Solution] TimescaleDB Distributed Foreign Table Error"
description: "How to fix TimescaleDB distributed foreign table errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Foreign table not created
- Data node not accessible
- Schema mismatch

## How to Fix

```sql
SELECT * FROM timescaledb_information.data_nodes;
```

## Examples

```sql
SELECT * FROM pg_foreign_server;
```
