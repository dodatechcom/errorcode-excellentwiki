---
title: "[Solution] TimescaleDB Distributed Restore Error"
description: "How to fix TimescaleDB distributed restore errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Restore failing on distributed cluster
- Backup format incompatible
- Data node not accessible

## How to Fix

```bash
pg_restore -D /backup/base -Fc
```

## Examples

```bash
pg_restore --list /backup/base/timescaledb.backup
```
