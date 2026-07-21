---
title: "[Solution] TimescaleDB Access Node Auth Error"
description: "How to fix TimescaleDB access node authentication errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Password authentication failing
- User not found on data node
- Auth method mismatch

## How to Fix

```sql
CREATE USER data_user WITH PASSWORD 'password';
GRANT ALL ON ALL TABLES IN SCHEMA public TO data_user;
```

## Examples

```sql
SELECT * FROM pg_stat_activity;
```
