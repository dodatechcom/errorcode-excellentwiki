---
title: "[Solution] TimescaleDB Access Node Permission Error"
description: "How to fix TimescaleDB access node permission errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- User not granted permissions on data node
- Foreign server permissions wrong
- Row-level security blocking

## How to Fix

```sql
GRANT USAGE ON FOREIGN SERVER data_node_1 TO myuser;
```

## Examples

```sql
SELECT * FROM pg_foreign_server;
```
