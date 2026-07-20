---
title: "[Solution] Redis MASTERDOWN Replica Stale Data Error"
description: "How to fix Redis MASTERDOWN error when replica-serve-stale-data is set to no"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Master is down and replica-serve-stale-data is set to no
- Replica is not serving any data during master outage
- Connection to master lost

## How to Fix

Check replica status:

```bash
redis-cli INFO replication | grep master_link_status
```

Check stale data setting:

```bash
redis-cli CONFIG GET replica-serve-stale-data
```

Temporarily allow stale data:

```bash
redis-cli CONFIG SET replica-serve-stale-data yes
```

Check master connection:

```bash
redis-cli INFO replication | grep master_host
```

## Examples

```bash
# Check master link status
redis-cli INFO replication | grep master_link_status

# Allow stale data temporarily
redis-cli CONFIG SET replica-serve-stale-data yes

# Check replica offset
redis-cli INFO replication | grep slave_repl_offset
```
