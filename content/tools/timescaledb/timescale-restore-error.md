---
title: "[Solution] TimescaleDB Restore Error — How to Fix"
description: "Fix TimescaleDB restore errors by resolving pg_restore failures, fixing extension reinstallation, and handling chunk restoration issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Restore Error

TimescaleDB restore errors occur when restoring from pg_basebackup, pg_dump, or continuous archiving backups. Extension installation and chunk restoration are common failure points.

## Why It Happens

- TimescaleDB extension is not installed on target server
- Backup was taken with different PostgreSQL version
- Continuous aggregate definitions are lost during restore
- Restore exceeds disk space on target
- Chunk data is corrupted in backup
- Restore process is interrupted

## Common Error Messages

```
ERROR: extension "timescaledb" does not exist
```

```
ERROR: incompatible backup version
```

```
ERROR: restore failed - disk full
```

```
ERROR: relation does not exist
```

## How to Fix It

### 1. Install TimescaleDB Extension First

```sql
-- On target server: install TimescaleDB
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- Verify installation
SELECT * FROM pg_extension WHERE extname = 'timescaledb';
```

### 2. Restore from pg_dump

```bash
# Restore from custom format dump
pg_restore -h localhost -p 5432 -U postgres \
  -d timescaledb -j 4 --no-owner --no-privileges \
  /backup/timescaledb.dump

# Restore with specific options
pg_restore -h localhost -p 5432 -U postgres \
  -d timescaledb --clean --if-exists \
  /backup/timescaledb.dump
```

### 3. Restore from pg_basebackup

```bash
# Stop PostgreSQL on target
sudo systemctl stop postgresql

# Clear existing data (CAUTION)
rm -rf /var/lib/postgresql/data/*

# Restore base backup
cp -r /backup/base/* /var/lib/postgresql/data/

# Configure recovery
cat > /var/lib/postgresql/data/postgresql.auto.conf << EOF
restore_command = 'cp /backup/wal/%f %p'
recovery_target_time = '2024-01-15 10:00:00'
EOF

# Create recovery signal
touch /var/lib/postgresql/data/recovery.signal

# Fix permissions
sudo chown -R postgres:postgres /var/lib/postgresql/data/

# Start PostgreSQL
sudo systemctl start postgresql
```

### 4. Verify Restore Success

```sql
-- Check hypertables are intact
SELECT * FROM timescaledb_information.hypertables;

-- Check continuous aggregates
SELECT * FROM timescaledb_information.continuous_aggregates;

-- Test data access
SELECT count(*) FROM sensor_data;

-- Check chunk count
SELECT count(*) FROM timescaledb_information.chunks
WHERE hypertable_name = 'sensor_data';
```

## Common Scenarios

- **Extension not found**: Install TimescaleDB extension before restoring data.
- **Chunk data missing**: Restore from base backup that includes chunk directories.
- **Continuous aggregate lost**: Recreate continuous aggregates after restore.

## Prevent It

- Always install TimescaleDB extension before restoring data
- Test restore procedures regularly
- Keep backup of continuous aggregate definitions separately

## Related Pages

- [TimescaleDB Backup Error](/tools/timescaledb/timescale-backup-error)
- [TimescaleDB Migration Error](/tools/timescaledb/timescale-migration-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
