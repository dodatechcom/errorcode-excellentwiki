---
title: "[Solution] TimescaleDB Access Node Schema Error"
description: "How to fix TimescaleDB access node schema errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Schema not synced between access and data nodes
- Schema mismatch
- Schema update not propagated

## How to Fix

```sql
SELECT * FROM timescaledb_information.data_nodes;
```

## Examples

```sql
SELECT * FROM pg_foreign_server;
```
