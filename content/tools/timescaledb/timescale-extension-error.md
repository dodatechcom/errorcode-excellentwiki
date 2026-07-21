---
title: "[Solution] TimescaleDB Extension Error — How to Fix"
description: "Fix TimescaleDB extension errors by resolving CREATE EXTENSION failures, fixing version conflicts, and handling extension upgrade issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Extension Error

TimescaleDB extension errors occur when creating, upgrading, or loading the TimescaleDB extension fails due to missing dependencies, version conflicts, or configuration issues.

## Why It Happens

- TimescaleDB shared library is not installed in the PostgreSQL lib directory
- Extension SQL files are missing or corrupted
- PostgreSQL version is incompatible with the TimescaleDB version
- Another extension conflicts with TimescaleDB
- Extension is created in the wrong database
- shared_preload_libraries does not include timescaledb

## Common Error Messages

```
ERROR: could not open extension control file
```

```
ERROR: extension "timescaledb" does not exist
```

```
ERROR: incompatible extension version
```

```
FATAL: timescaledb is not in shared_preload_libraries
```

## How to Fix It

### 1. Verify Installation

```bash
# Check if timescaledb is in shared_preload_libraries
SHOW shared_preload_libraries;

# Check installed files
ls /usr/lib/postgresql/*/lib/timescaledb*

# Check extension SQL files
ls /usr/share/postgresql/*/extension/timescaledb*
```

### 2. Configure shared_preload_libraries

```bash
# Edit postgresql.conf
shared_preload_libraries = 'timescaledb'

# Restart PostgreSQL
sudo systemctl restart postgresql

# Verify after restart
SHOW shared_preload_libraries;
```

### 3. Create the Extension

```sql
-- Create TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- Check extension version
SELECT * FROM pg_extension
WHERE extname = 'timescaledb';

-- Upgrade extension
ALTER EXTENSION timescaledb UPDATE;
```

### 4. Fix Version Conflicts

```sql
-- Check current version
SELECT extversion FROM pg_extension
WHERE extname = 'timescaledb';

-- Check available versions
SELECT * FROM pg_available_extensions
WHERE name = 'timescaledb';

-- Downgrade if needed (requires dump/restore)
-- pg_dump the database, reinstall correct version, pg_restore
```

## Common Scenarios

- **Extension fails to load after install**: Ensure shared_preload_libraries is set and restart PostgreSQL.
- **Version mismatch after upgrade**: Run ALTER EXTENSION timescaledb UPDATE.
- **Extension works in one database but not another**: CREATE EXTENSION must be run in each database.

## Prevent It

- Install the correct TimescaleDB version for your PostgreSQL version
- Add timescaledb to shared_preload_libraries before creating the extension
- Test extension creation in a test database first

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
- [TimescaleDB Install Error](/tools/timescaledb/timescale-install-error)
