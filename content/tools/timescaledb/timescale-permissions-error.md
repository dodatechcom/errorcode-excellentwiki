---
title: "[Solution] TimescaleDB Permissions Error — How to Fix"
description: "Fix TimescaleDB permission errors by resolving access denied issues, fixing role grants for hypertables, and handling background worker permissions"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Permissions Error

TimescaleDB permission errors occur when users lack the required privileges to perform operations on hypertables, continuous aggregates, or TimescaleDB-specific functions.

## Why It Happens

- User does not have CREATE privilege on the schema
- User cannot call TimescaleDB-specific functions
- Continuous aggregate refresh requires elevated privileges
- Chunk operations need table-level permissions
- Background worker lacks schema ownership
- ALTER on hypertable requires owner privileges

## Common Error Messages

```
ERROR: permission denied for table sensor_data
```

```
ERROR: must be owner of hypertable
```

```
ERROR: permission denied for function create_hypertable
```

```
ERROR: must be superuser to use continuous aggregates
```

## How to Fix It

### 1. Grant Basic Permissions

```sql
-- Grant schema usage
GRANT USAGE ON SCHEMA public TO app_user;

-- Grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON sensor_data TO app_user;

-- Grant hypertable function permissions
GRANT EXECUTE ON FUNCTION create_hypertable TO app_user;
```

### 2. Grant Continuous Aggregate Permissions

```sql
-- Grant privileges for continuous aggregates
GRANT SELECT ON sensor_data TO reporting_user;
GRANT USAGE ON SCHEMA public TO reporting_user;

-- Allow refresh (requires elevated privileges)
GRANT EXECUTE ON FUNCTION refresh_continuous_aggregate TO admin_user;
```

### 3. Fix Background Worker Permissions

```sql
-- Ensure TimescaleDB functions are accessible
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO public;

-- Check background worker status
SELECT * FROM timescaledb_information.jobs;
```

### 4. Create Role-Based Access

```sql
-- Create role for hypertable operations
CREATE ROLE hypertable_admin;
GRANT ALL ON sensor_data TO hypertable_admin;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO hypertable_admin;

-- Assign role to user
GRANT hypertable_admin TO app_admin;
```

## Common Scenarios

- **User cannot query hypertable**: Grant SELECT on the hypertable and all chunks.
- **Continuous aggregate refresh fails**: Grant EXECUTE on the refresh function.
- **Background worker fails**: Ensure the TimescaleDB extension owner has proper schema permissions.

## Prevent It

- Use role-based access control for hypertable operations
- Grant minimal required privileges to application users
- Test permission changes in a staging environment

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB Hypertable Error](/tools/timescaledb/timescale-hypertable-error)
