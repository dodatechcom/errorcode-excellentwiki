---
title: "[Solution] TimescaleDB Distributed Insert Error"
description: "How to fix TimescaleDB distributed insert errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Insert failed on data node
- Data node unreachable
- Insert timeout

## How to Fix

```sql
INSERT INTO conditions VALUES (now(), 1, 23.5);
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
