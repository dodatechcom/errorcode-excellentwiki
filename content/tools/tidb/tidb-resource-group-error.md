---
title: "[Solution] TiDB Resource Group Error — How to Fix"
description: "Fix TiDB resource group errors by resolving resource control configuration issues, fixing priority assignment failures, and handling quota exceeded"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Resource Group Error

TiDB resource group errors occur when the resource control feature fails to manage CPU and I/O resources for workloads, including priority assignment and quota enforcement.

## Why It Happens

- Resource control is not enabled in TiDB configuration
- Specified resource group does not exist
- RU (Resource Unit) quota is exceeded for the group
- User is not assigned to any resource group
- Background tasks are not correctly bound to resource groups
- Resource group configuration conflicts with global settings

## Common Error Messages

```
ERROR: resource group not found
```

```
ERROR: resource control is not enabled
```

```
ERROR: RU quota exceeded for group
```

```
ERROR: cannot bind session to resource group
```

## How to Fix It

### 1. Enable Resource Control

```toml
# tidb.toml
[resource-control]
# Enable resource control
enabled = true
# RU refresh interval
ru-refresh-interval = "1s"
#RU cleanup interval
ru-cleanup-period = "10s"
```

```sql
-- Check if resource control is enabled
SHOW VARIABLES LIKE 'tidb_resource_control%';
```

### 2. Create and Configure Resource Groups

```sql
-- Create a resource group with RU limit
CREATE RESOURCE GROUP high_priority
  RU_PER_SEC = 5000
  PRIORITY = HIGH;

CREATE RESOURCE GROUP low_priority
  RU_PER_SEC = 1000
  PRIORITY = LOW;

-- Alter an existing resource group
ALTER RESOURCE GROUP high_priority
  RU_PER_SEC = 10000;

-- Check resource groups
SELECT * FROM information_schema.resource_groups;
```

### 3. Assign Users to Resource Groups

```sql
-- Assign user to resource group
ALTER USER 'app_user'@'%' RESOURCE GROUP high_priority;

-- Assign default resource group for a session
SET RESOURCE GROUP high_priority;

-- Check user resource group
SELECT user, resource_group FROM mysql.user;
```

### 4. Handle RU Quota Exceeded

```sql
-- Monitor resource group usage
SELECT * FROM information_schema.resource_group_usage;

-- Increase RU quota for the group
ALTER RESOURCE GROUP app_group RU_PER_SEC = 20000;

-- Check which group is throttling
SELECT * FROM information_schema.CLUSTER_TIDB_TRX
WHERE resource_group_name = 'app_group';
```

## Common Scenarios

- **Queries are slow despite low load**: The resource group RU quota may be too low; increase it.
- **Background job affects production**: Move the job to a low-priority resource group.
- **Cannot create resource group**: Ensure `tidb_resource_control_enabled` is set to ON.

## Prevent It

- Define resource groups during cluster setup
- Monitor RU consumption per group regularly
- Set appropriate priority levels for different workload types

## Related Pages

- [TiDB Config Error](/tools/tidb/tidb-system-variable-error)
- [TiDB OOM Error](/tools/tidb/tidb-oom-error)
- [TiDB Metrics Error](/tools/tidb/tidb-metrics-error)
