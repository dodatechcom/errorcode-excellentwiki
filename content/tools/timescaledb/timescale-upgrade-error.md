---
title: "[Solution] TimescaleDB Upgrade Error — How to Fix"
description: "Fix TimescaleDB upgrade errors by resolving extension update failures, fixing version compatibility, and handling schema migration issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Upgrade Error

TimescaleDB upgrade errors occur when updating the TimescaleDB extension, PostgreSQL version, or migrating data between versions.

## Why It Happens

- Extension update fails due to incompatible API changes
- PostgreSQL version is not supported by target TimescaleDB
- Continuous aggregates are incompatible after upgrade
- Database has active connections during upgrade
- Schema changes required by new version fail
- Upgrade script encounters locked tables

## Common Error Messages

```
ERROR: extension update failed
```

```
ERROR: incompatible TimescaleDB version
```

```
ERROR: continuous aggregate incompatible after upgrade
```

```
ERROR: cannot update extension with active connections
```

## How to Fix It

### 1. Check Current Versions

```sql
-- Check TimescaleDB version
SELECT * FROM pg_extension WHERE extname = 'timescaledb';

-- Check PostgreSQL version
SELECT version();

-- Check extension update path
SELECT * FROM pg_available_extension_versions
WHERE name = 'timescaledb';
```

### 2. Upgrade TimescaleDB Extension

```sql
-- Upgrade to latest version
ALTER EXTENSION timescaledb UPDATE;

-- Upgrade to specific version
ALTER EXTENSION timescaledb UPDATE TO '2.14.0';

-- Verify upgrade
SELECT * FROM pg_extension WHERE extname = 'timescaledb';
```

### 3. Fix Upgrade Failures

```bash
# Stop all connections before upgrade
sudo systemctl stop postgresql

# Start in single-user mode for emergency upgrade
postgres --single -D /var/lib/postgresql/data

# Or use timescaledb-upgrade tool
timescaledb-upgrade --dry-run
timescaledb-upgrade
```

### 4. Validate After Upgrade

```sql
-- Verify hypertables are intact
SELECT * FROM timescaledb_information.hypertables;

-- Verify continuous aggregates
SELECT * FROM timescaledb_information.continuous_aggregates;

-- Verify compression policies
SELECT * FROM timescaledb_information.jobs;

-- Test a simple query
SELECT * FROM sensor_data LIMIT 1;
```

## Common Scenarios

- **Extension update fails**: Ensure no active connections and retry.
- **Continuous aggregate broken after upgrade**: Recreate the view with new syntax.
- **PostgreSQL version mismatch**: Upgrade PostgreSQL first, then TimescaleDB.

## Prevent It

- Test upgrades on a staging environment first
- Back up the database before any upgrade
- Read release notes for breaking changes

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB 1 Node Error](/tools/timescaledb/timescale-1-node-error)
