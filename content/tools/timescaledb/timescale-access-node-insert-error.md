---
title: "[Solution] TimescaleDB Access Node Insert Error"
description: "How to fix TimescaleDB access node insert errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Insert not reaching data node
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
