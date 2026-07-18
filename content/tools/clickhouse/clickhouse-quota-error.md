---
title: "[Solution] ClickHouse Quota Error — How to Fix"
description: "Fix ClickHouse quota errors including query limits exceeded, resource quota violations, and quota configuration issues"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Quota Error

Quota errors in ClickHouse occur when users exceed their configured resource limits. Quotas control the amount of resources (queries, rows read, execution time) a user can consume.

## Why It Happens

- The user has exceeded the maximum number of queries per time interval
- The user has read more rows than the quota allows
- The query execution time exceeds the quota limit
- The quota configuration is too restrictive for the workload
- Multiple queries from the same user exhaust the shared quota
- The quota is applied to the wrong user or role

## Common Error Messages

```
Code: 195. DB::Exception: Quota for user 'myuser' has been exceeded
```

```
Code: 195. DB::Exception: Limit exceeded: quota 'default' has been exceeded
```

```
Code: 195. DB::Exception: Too many queries. Quota exceeded
```

```
Code: 202. DB::Exception: Too many simultaneous queries. Quota exceeded
```

## How to Fix It

### 1. Check Current Quotas

```sql
-- Show quota settings
SHOW QUOTAS;

-- Show quota usage
SELECT * FROM system.quota_usage;
```

### 2. Increase or Modify Quota

```sql
-- Create a new quota with higher limits
CREATE QUOTA IF NOT EXISTS my_quota
  FOR INTERVAL 1 hour MAX queries = 10000, MAX rows = 100000000, MAX execution_time = 300
  TO 'myuser'@'192.168.1.%';
```

### 3. Fix Quota Configuration

```xml
<!-- In /etc/clickhouse-server/users.d/quota.xml -->
<clickhouse>
  <quotas>
    <my_quota>
      <limits>
        <interval>
          <min>0</min>
          <max>1</max>
          <duration>3600</duration>
          <queries>10000</queries>
          <errors>100</errors>
          <result_rows>100000000</result_rows>
          <read_rows>200000000</read_rows>
          <execution_time>300</execution_time>
        </interval>
      </limits>
    </my_quota>
  </quotas>
</clickhouse>
```

### 4. Reset Quota for Specific User

```sql
-- Reset quota counters
SYSTEM DROP QUOTA my_quota;
-- Recreate with fresh counters

-- Or create a temporary exception quota
CREATE QUOTA temp_exception FOR INTERVAL 1 hour MAX queries = 50000 TO 'myuser'@'192.168.1.%';
```

## Common Scenarios

- **ETL job exceeds row quota**: Increase row limit for the ETL user or run during off-peak hours.
- **Dashboard query times out**: Increase execution_time limit for the dashboard user.
- **Multiple services share a quota**: Create separate quotas for each service.

## Prevent It

- Monitor quota usage with `system.quota_usage`
- Create separate quotas for different workloads (ETL, dashboards, ad-hoc)
- Set reasonable defaults and adjust based on actual usage patterns

## Related Pages

- [ClickHouse User Error](/tools/clickhouse/clickhouse-user-error)
- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse Memory Error](/tools/clickhouse/clickhouse-memory-error)
