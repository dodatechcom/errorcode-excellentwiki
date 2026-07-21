---
title: "[Solution] TimescaleDB Version Error — How to Fix"
description: "Fix TimescaleDB version errors by resolving version mismatch issues, fixing upgrade failures, and handling incompatible extension versions"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Version Error

TimescaleDB version errors occur when there is a mismatch between the installed TimescaleDB version, the PostgreSQL version, or when upgrading between TimescaleDB major versions.

## Why It Happens

- TimescaleDB version does not match the PostgreSQL version
- Extension was created with a newer version than installed
- Upgrade script fails midway leaving partial upgrade
- Shared library version does not match SQL extension version
- Docker image uses a different version than expected
- Multiple databases have different TimescaleDB versions

## Common Error Messages

```
ERROR: extension version mismatch
```

```
ERROR: timescaledb.so version does not match SQL
```

```
ERROR: incompatible extension update path
```

```
FATAL: incompatible TimescaleDB version
```

## How to Fix It

### 1. Check Current Version

```sql
-- Check installed extension version
SELECT extname, extversion
FROM pg_extension
WHERE extname = 'timescaledb';

-- Check shared library version
SHOW shared_preload_libraries;

-- Check version from SQL
SELECT * FROM timescaledb_information.license;
```

### 2. Fix Version Mismatch

```sql
-- Update extension to latest available version
ALTER EXTENSION timescaledb UPDATE;

-- If update fails, check available versions
SELECT * FROM pg_available_extensions
WHERE name = 'timescaledb';
```

### 3. Upgrade TimescaleDB Major Version

```bash
# Stop PostgreSQL
sudo systemctl stop postgresql

# Install new TimescaleDB package
sudo apt-get install timescaledb-2-postgresql-14

# Update shared_preload_libraries
echo "shared_preload_libraries = 'timescaledb'" | \
  sudo tee /etc/postgresql/*/main/postgresql.conf

# Start PostgreSQL
sudo systemctl start postgresql

# Update extension in each database
psql -d mydb -c "ALTER EXTENSION timescaledb UPDATE;"
```

### 4. Fix Partial Upgrade

```sql
-- Check upgrade status
SELECT * FROM _timescaledb_catalog.timescaledb_version;

-- If stuck, try reinstalling the extension
-- WARNING: backup data first
DROP EXTENSION timescaledb CASCADE;
CREATE EXTENSION timescaledb;
```

## Common Scenarios

- **Extension version mismatch after install**: Run ALTER EXTENSION timescaledb UPDATE.
- **Upgrade fails midway**: Restore from backup and retry upgrade.
- **Docker version mismatch**: Pull the correct Docker image tag.

## Prevent It

- Match TimescaleDB version to PostgreSQL version exactly
- Test upgrades in staging before production
- Keep backups before any version upgrade

## Related Pages

- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
- [TimescaleDB Extension Error](/tools/timescaledb/timescale-extension-error)
- [TimescaleDB Install Error](/tools/timescaledb/timescale-install-error)
