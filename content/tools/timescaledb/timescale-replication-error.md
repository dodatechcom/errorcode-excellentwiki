---
title: "[Solution] TimescaleDB Replication Error — How to Fix"
description: "Fix TimescaleDB replication errors by resolving streaming replication failures, fixing WAL issues, and handling standby node synchronization"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Replication Error

TimescaleDB replication errors occur when streaming replication between primary and standby nodes fails, causing data inconsistency or standby unavailability.

## Why It Happens

- Standby node falls behind primary (WAL accumulation)
- Replication slot is not created or is dropped
- Network partition prevents WAL shipping
- Primary runs out of disk space for WAL files
- Replication timeout expires on standby
- Timeline diverges between primary and standby

## Common Error Messages

```
ERROR: WAL receiver process not running
```

```
ERROR: could not receive data from WAL stream
```

```
ERROR: replication slot not found
```

```
ERROR: standby replication timeout expired
```

## How to Fix It

### 1. Check Replication Status

```sql
-- On primary: check replication state
SELECT
  client_addr,
  state,
  sent_lsn,
  write_lsn,
  flush_lsn,
  replay_lsn,
  (sent_lsn - replay_lsn) AS replication_lag
FROM pg_stat_replication;

-- Check replication slots
SELECT
  slot_name,
  active,
  restart_lsn,
  confirmed_flush_lsn
FROM pg_replication_slots;
```

### 2. Fix WAL Shipping Issues

```sql
-- Ensure WAL level is set correctly
SHOW wal_level;

-- Should be 'replica' or 'logical'
ALTER SYSTEM SET wal_level = 'replica';
SELECT pg_reload_conf();

-- Check WAL archiving status
SELECT * FROM pg_stat_archiver;
```

### 3. Create Replication Slot

```sql
-- Create physical replication slot
SELECT pg_create_physical_replication_slot('standby1_slot');

-- On standby: configure primary_slot_name
-- In postgresql.conf:
-- primary_slot_name = 'standby1_slot'
```

### 4. Restart Standby Replication

```bash
# On standby: check WAL receiver
pg_ctl status -D /var/lib/postgresql/data

# If stopped, restart
pg_ctl start -D /var/lib/postgresql/data

# Check standby logs for errors
tail -50 /var/lib/postgresql/data/log/postgresql-*.log
```

## Common Scenarios

- **Standby replication lag**: Check network bandwidth and WAL generation rate.
- **WAL files fill disk on primary**: Increase wal_keep_size or use replication slots.
- **Standby cannot connect**: Verify pg_hba.conf allows replication connections.

## Prevent It

- Monitor replication lag with alerts
- Use replication slots to prevent premature WAL cleanup
- Ensure adequate network bandwidth between primary and standby

## Related Pages

- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Backup Error](/tools/timescaledb/timescale-backup-error)
