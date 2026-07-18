---
title: "Fix Vitess Shard Error — How to Fix"
description: "Resolve Vitess shard errors by checking shard configuration and health"
tools: ["vitess"]
error-types: ["vitess-shard-error"]
severities: ["warning"]
weight: 18
comments:
  - "Check shard status"
  - "Verify shard topology"
---

# Vitess Shard Error — How to Fix

## Why It Happens

Shard errors occur when Vitess cannot manage a shard properly due to configuration issues, tablet failures, or topology problems that prevent the shard from functioning correctly.

## Common Error Messages

- `shard error: no healthy tablets`
- `shard error: replication not running`
- `shard error: primary not found`
- `shard error: tablet not serving`

## How to Fix It

### 1. Check shard status

Verify the shard health:

```bash
# List shards
vtctldclient list_shards --server localhost:15999

# Get shard details
vtctldclient get_shard --server localhost:15999 <keyspace>/<shard>

# Check shard tablets
vtctldclient list-tablets --server localhost:15999 | grep <shard>
```

### 2. Verify primary tablet

Ensure shard has a healthy primary:

```bash
# Check primary tablet
vtctldclient get_shard --server localhost:15999 <keyspace>/<shard> | grep primary

# If no primary, check tablet roles
vtctldclient list-tablets --server localhost:15999
```

### 3. Check replication health

Verify replication is running:

```sql
-- On replica tablet
SHOW SLAVE STATUS\G

-- Check replication lag
SHOW SLAVE STATUS\G | grep Seconds_Behind_Master
```

### 4. Restart shard tablets

If tablets are unhealthy:

```bash
# Check tablet health
vtctldclient list-tablets --server localhost:15999

# Restart unhealthy tablets
systemctl restart vitess-vttablet
```

## Common Scenarios

**Scenario 1: No primary tablet**

If shard has no primary:

```bash
# Check tablet roles
vtctldclient list-tablets --server localhost:15999

# If no primary, perform planned reparent
vtctldclient planned_reparent_shard --server localhost:15999 <keyspace>/<shard>
```

**Scenario 2: Shard split issues**

If shard split failed:

```bash
# Check shard configuration
vtctldclient get_keyspace --server localhost:15999 <keyspace>

# Verify shards exist
vtctldclient list_shards --server localhost:15999
```

## Prevent It

1. Monitor shard health metrics
2. Set up proper alerting for shard issues
3. Regularly verify shard configuration

## Related Pages

- [Vitess Tablet Error](vitess-tablet-error)
- [Vitess Replication Error](vitess-replication-error)
- [Vitess Keyspace Error](vitess-keyspace-error)
