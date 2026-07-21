---
title: "[Solution] YugabyteDB Resource Group Error — How to Fix"
description: "Fix YugabyteDB resource group errors by resolving resource management failures, fixing workload prioritization, and handling CPU/memory allocation issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Resource Group Error

YugabyteDB resource group errors occur when workload management or resource allocation fails, causing queries to be throttled, denied, or to consume excessive resources.

## Why It Happens

- Resource group is not defined for the user
- CPU or memory limits are exceeded
- Query priority conflicts with resource allocation
- Resource group configuration has invalid parameters
- Background worker resource limits are too low
- Concurrent queries exceed total resource group capacity

## Common Error Messages

```
ERROR: resource group not found
```

```
ERROR: CPU quota exceeded for resource group
```

```
ERROR: memory limit exceeded
```

```
WARNING: query throttled by resource group
```

## How to Fix It

### 1. Check Resource Groups

```sql
-- Check resource group settings
SHOW yb_enable_resource_groups;

-- Enable resource groups
SET yb_enable_resource_groups = on;
```

### 2. Configure Resource Groups

```sql
-- Create resource group
CREATE RESOURCE GROUP high_priority
  WITH (concurrency = 10, cpu_rate_limit = 0.5);

-- Assign user to resource group
ALTER USER app_user RESOURCE GROUP high_priority;

-- Check resource group assignments
SELECT * FROM pg_resource_groups;
```

### 3. Monitor Resource Usage

```sql
-- Check resource group metrics
SELECT * FROM yb_tserver_metrics
WHERE metric LIKE '%resource_group%';

-- Check query resource consumption
SELECT * FROM pg_stat_activity
WHERE state = 'active';
```

### 4. Adjust Resource Limits

```sql
-- Increase CPU limit
ALTER RESOURCE GROUP high_priority
  WITH (cpu_rate_limit = 0.8);

-- Increase concurrency
ALTER RESOURCE GROUP high_priority
  WITH (concurrency = 20);
```

## Common Scenarios

- **Query is throttled**: Increase resource limits for the user's resource group.
- **Resource group not found**: Create the resource group before assigning users.
- **CPU quota exceeded**: Increase cpu_rate_limit for the resource group.

## Prevent It

- Configure resource groups before workload peaks
- Monitor resource group usage regularly
- Set appropriate limits for different workload types

## Related Pages

- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-config-error)
- [YugabyteDB Query Error](/tools/yugabyte/yugabyte-query-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
