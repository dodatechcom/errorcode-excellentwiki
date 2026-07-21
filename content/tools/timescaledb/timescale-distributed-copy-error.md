---
title: "[Solution] TimescaleDB Distributed Copy Error"
description: "How to fix TimescaleDB distributed COPY errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- COPY failing on distributed hypertable
- Data node unreachable
- Data format wrong

## How to Fix

```sql\nCOPY conditions FROM STDIN;
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
