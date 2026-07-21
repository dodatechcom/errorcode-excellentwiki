---
title: "[Solution] TimescaleDB License Error — How to Fix"
description: "Fix TimescaleDB license errors by resolving license key validation failures, fixing community edition limitations, and handling enterprise license issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB License Error

TimescaleDB license errors occur when the license key is invalid, expired, or when enterprise features are used without a valid license.

## Why It Happens

- License key format is incorrect
- License has expired
- Enterprise feature is used on community edition
- License is tied to a different machine or cluster
- License file was not loaded during startup
- Multiple license keys conflict

## Common Error Messages

```
ERROR: invalid license key format
```

```
ERROR: license has expired
```

```
ERROR: feature requires TimescaleDB License
```

```
WARNING: running without a license
```

## How to Fix It

### 1. Check License Status

```sql
-- Check current license
SELECT * FROM timescaledb_information.license;

-- Check available features
SHOW timescaledb.license;

-- Check license expiry
SELECT
  license_key,
  license_type,
  expiry_time
FROM _timescaledb_config.bgw_job;
```

### 2. Apply License Key

```sql
-- Set the license key
ALTER SYSTEM SET timescaledb.license_key = 'YOUR_LICENSE_KEY';
SELECT pg_reload_conf();

-- Verify
SHOW timescaledb.license;
```

### 3. Switch Between Editions

```sql
-- Use community edition (Apache-2.0)
ALTER SYSTEM SET timescaledb.license = 'community';
SELECT pg_reload_conf();

-- Use timescale license (Timescale License)
ALTER SYSTEM SET timescaledb.license = 'timescale';
SELECT pg_reload_conf();
```

### 4. Fix License Key Format

```bash
# License key format: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
# Ensure no extra spaces or characters
echo "YOUR_LICENSE_KEY" | tr -d '[:space:]'

# Check license in configuration
grep license_key /etc/timescaledb/timescaledb.conf
```

## Common Scenarios

- **Feature requires license**: Upgrade from community to enterprise or timescale license.
- **License expired**: Renew the license and apply the new key.
- **Running without license**: Apply a valid license key to enable all features.

## Prevent It

- Store license keys securely and track expiration dates
- Test license application in staging before production
- Monitor license status as part of regular maintenance

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Extension Error](/tools/timescaledb/timescale-extension-error)
- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
