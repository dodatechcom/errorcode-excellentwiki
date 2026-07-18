---
title: "[Solution] TimescaleDB Replication Error — How to Fix"
description: "Fix TimescaleDB replication errors by resolving streaming replication failures, fixing standby configuration, and handling WAL issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Replication Error

TimescaleDB replication errors occur when streaming replication between primary and standby nodes fails. Replication ensures high availability and read scaling.

## Why It Happens

- Standby cannot connect to primary for WAL streaming
- Replication slot is not created or is full
- WAL retention is insufficient for standby lag
- Network bandwidth is saturated by replication traffic
- Primary and standby PostgreSQL versions mismatch
- pg_hba.conf rejects replication connections

## Common Error Messages

```
ERROR: could not connect to primary server
```

```
ERROR: replication slot not found
```

```
ERROR: WAL retention exceeded
```

```
FATAL: replication connection authorization failed
```

## How to Fix It

### 1. Check Replication Status

```sql
-- On primary: check replication status
SELECT * FROM pg_stat_replication;

-- Check replication slots
SELECT * FROM pg_replication_slots;

-- Check WAL position
SELECT pg_current_wal_lsn();
```

### 2. Create Replication Slot

```sql
-- On primary: create replication slot
SELECT pg_create_physical_replication_slot('standby_slot');

-- On standby: configure slot
-- In postgresql.auto.conf:
-- primary_slot_name = 'standby_slot'
```

### 3. Fix Standby Configuration

```bash
# On standby: configure recovery
cat > /var/lib/postgresql/data/postgresql.auto.conf << EOF
primary_conninfo = 'host=10.0.0.1 port=5432 user=replicator password=secret'
primary_slot_name = 'standby_slot'
EOF

# Create standby signal file
touch /var/lib/postgresql/data/standby.signal

# Restart standby
sudo systemctl restart postgresql
```

### 4. Fix WAL Retention

```sql
-- On primary: increase WAL retention
ALTER SYSTEM SET max_replication_slots = 10;
ALTER SYSTEM SET wal_keep_size = '1GB';
SELECT pg_reload_conf();

-- Monitor replication lag
SELECT
  client_addr,
  state,
  sent_lsn,
  write_lsn,
  replay_lsn,
  pg_wal_lsn_diff(sent_lsn, replay_lsn) AS replication_lag_bytes
FROM pg_stat_replication;
```

## Common Scenarios

- **Standby falls behind**: Increase `wal_keep_size` on primary.
- **Replication slot fills up**: Drop unused slots and monitor slot size.
- **Standby cannot reconnect**: Check `pg_hba.conf` and `primary_conninfo`.

## Prevent It

- Monitor replication lag with `pg_stat_replication`
- Set up alerts for replication lag exceeding thresholds
- Regularly clean up unused replication slots

## Related Pages

- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
