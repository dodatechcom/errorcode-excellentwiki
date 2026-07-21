---
title: "[Solution] TimescaleDB Distributed Backup Error"
description: "How to fix TimescaleDB distributed backup errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Backup failing on distributed cluster
- Data node unreachable
- Backup storage not accessible

## How to Fix

```bash
pg_basebackup -h data-node -D /backup/base -Ft -z -P
```

## Examples

```sql
SELECT * FROM timescaledb_information.data_nodes;
```
