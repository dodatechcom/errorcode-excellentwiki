---
title: "[Solution] TimescaleDB License Error — How to Fix"
description: "Fix TimescaleDB license errors by activating trial licenses, resolving community edition limitations, and fixing expired license issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB License Error

TimescaleDB license errors occur when attempting to use features restricted to specific license tiers (Community, Standard, Enterprise).

## Why It Happens

- Using Enterprise features without an Enterprise license
- License has expired
- License server is unreachable for validation
- Community edition limitations are exceeded
- License is tied to a different host
- Multi-node features require paid license

## Common Error Messages

```
ERROR: function is only available on Timescale Cloud or with a Timescale License
```

```
ERROR: license expired
```

```
ERROR: feature not available in community edition
```

```
ERROR: license validation failed
```

## How to Fix It

### 1. Check Current License

```sql
-- Check TimescaleDB license
SHOW timescaledb.license;

-- Check extension version
SELECT * FROM pg_extension WHERE extname = 'timescaledb';
```

### 2. Activate License

```sql
-- Set license key (Enterprise/Standard)
ALTER SYSTEM SET timescaledb.license = 'enterprise';
SELECT pg_reload_conf();

-- For community edition (Apache 2.0)
ALTER SYSTEM SET timescaledb.license = 'community';
SELECT pg_reload_conf();
```

### 3. Use Community Features

```sql
-- Community edition supports:
-- Single-node hypertables
-- Compression
-- Continuous aggregates (basic)
-- Data retention policies

-- Enterprise features NOT in community:
-- Multi-node (distributed hypertables)
-- Data node management
-- Advanced compression
-- Continuous aggregates (advanced)
```

### 4. Fix License Validation

```bash
# If license server is unreachable, check network
curl -I https://license.timescale.com

# For air-gapped environments, contact Timescale support
# for offline license activation

# Check license file location
ls -la /etc/timescaledb/license*
```

## Common Scenarios

- **Trial license expired**: Request extension from Timescale or upgrade to paid.
- **Multi-node not available**: Requires Enterprise license.
- **Feature not found**: Check if feature requires paid license.

## Prevent It

- Understand license tier requirements before deploying features
- Set up license expiration monitoring
- Use community edition features only for open-source deployments

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Multinode Error](/tools/timescaledb/timescale-multinode-error)
- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
