---
title: "Fix Vitess Reparent Error — How to Fix"
description: "Resolve Vitess reparent errors by checking tablet roles and replication state"
tools: ["vitess"]
error-types: ["vitess-reparent-error"]
severities: ["warning"]
weight: 31
comments:
  - "Check tablet roles"
  - "Verify replication state"
---

# Vitess Reparent Error — How to Fix

## Why It Happens

Reparent errors occur when Vitess cannot perform primary failover or planned reparent due to tablet issues, replication problems, or topology conflicts.

## Common Error Messages

- `reparent error: no healthy replica`
- `reparent error: replication lag too high`
- `reparent error: failed to promote tablet`
- `reparent error: tablet not in good state`

## How to Fix It

### 1. Check tablet roles

Verify current tablet roles:

```bash
# List tablets and roles
vtctldclient list-tablets --server localhost:15999

# Check primary tablet
vtctldclient get_shard --server localhost:15999 <keyspace>/<shard> | grep primary
```

### 2. Verify replication health

Check replication status:

```sql
-- On replica tablet
SHOW SLAVE STATUS\G

-- Check replication lag
SHOW SLAVE STATUS\G | grep Seconds_Behind_Master
```

### 3. Check tablet health

Ensure tablets are healthy:

```bash
# Check tablet health
vtctldclient get-tablet <tablet-alias> --server localhost:15999

# Check tablet flags
ps aux | grep vttablet
```

### 4. Perform reparent

If reparent is needed:

```bash
# Planned reparent (preferred)
vtctldclient planned_reparent_shard --server localhost:15999 <keyspace>/<shard>

# Emergency reparent (if primary down)
vtctldclient emergency_reparent_shard --server localhost:15999 <keyspace>/<shard>
```

## Common Scenarios

**Scenario 1: Primary down**

If primary tablet is down:

```bash
# Check primary status
vtctldclient get_shard --server localhost:15999 <keyspace>/<shard>

# Perform emergency reparent
vtctldclient emergency_reparent_shard --server localhost:15999 <keyspace>/<shard>
```

**Scenario 2: Replication lag too high**

If replica lag prevents reparent:

```sql
-- Check lag
SHOW SLAVE STATUS\G | grep Seconds_Behind_Master

-- Wait for lag to decrease
-- Or skip to another replica
```

## Prevent It

1. Monitor tablet health
2. Regularly test failover
3. Set up proper alerting

## Related Pages

- [Vitess Replication Error](vitess-replication-error)
- [Vitess Tablet Error](vitess-tablet-error)
- [Vitess Shard Error](vitess-shard-error)
