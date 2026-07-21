---
title: "[Solution] PostgreSQL Standby Mode Recovery Error"
description: "Fix PostgreSQL standby mode recovery errors. Resolve issues with standby server failing to follow primary."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Standby Mode Recovery Error

ERROR: standby mode is not supported by this server version

This error occurs when the standby server cannot enter or maintain streaming replication recovery mode.

## Common Causes

- recovery.conf file is missing or misconfigured on the standby
- WAL sender on the primary is not running
- Network connectivity issues between primary and standby
- Incompatible PostgreSQL versions between nodes

## How to Fix

1. Check if the standby has a valid recovery configuration:

```bash
cat /var/lib/postgresql/*/main/recovery.conf
```

2. Verify WAL level on the primary:

```sql
SHOW wal_level;
-- Should be 'replica' or 'logical'
```

3. Initialize a new standby using pg_basebackup:

```bash
pg_basebackup -h primary_host -D /var/lib/postgresql/data \
  -U replicator -P -R
```

4. Verify replication status on the primary:

```sql
SELECT client_addr, state, sent_lsn, replay_lsn,
       replay_lag FROM pg_stat_replication;
```

## Examples

```bash
# Force promote a standby to primary
pg_ctl promote -D /var/lib/postgresql/data
```
