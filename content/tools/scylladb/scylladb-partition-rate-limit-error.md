---
title: "[Solution] ScyllaDB Per-Partition Rate Limit Error — How to Fix"
description: "Fix ScyllaDB per-partition rate limit errors when individual partitions receive too many operations"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Per-Partition Rate Limit Error

Per-partition rate limit errors occur when ScyllaDB throttles operations on individual partitions that exceed the configured rate limit, protecting the cluster from hotspot issues.

## Why It Happens

- A single partition receives disproportionate traffic
- Hot partition due to poor data distribution
- Rate limit is set too low for the workload
- Client retries amplify the load on the same partition
- Large partition with many tombstones triggers slow reads

## Common Error Messages

```
Rate limit exceeded for partition key in table mykeyspace.events
```

```
ScyllaPerPartitionRateLimit: request throttled, retry after 100ms
```

```
error: partition rate limit reached for table users
```

## How to Fix It

### 1. Check Current Rate Limits

```bash
nodetool tableproperties mykeyspace users | grep rate_limit
```

### 2. Adjust Rate Limit

```cql
ALTER TABLE mykeyspace.events 
  WITH per_partition_rate_limit = {'mode': 'writes', 'max_writes_per_second': 10000};
```

### 3. Disable Rate Limiting (Not Recommended for Production)

```cql
ALTER TABLE mykeyspace.events 
  WITH per_partition_rate_limit = {'mode': 'disabled'};
```

### 4. Redesign to Distribute Load

```cql
-- Add a random shard key to distribute writes
INSERT INTO events (event_id, partition_key, data) 
  VALUES (uuid(), concat('shard_', randomInt(0, 99)), 'data');
```

## Examples

```
$ nodetool tableproperties mykeyspace events | grep rate
  per_partition_rate_limit: writes, 5000 ops/sec
```

## Prevent It

- Design data models to avoid hot partitions
- Monitor per-partition operation rates
- Adjust rate limits based on observed traffic patterns

## Related Pages

- [ScyllaDB Per Partition Rate Limit](/tools/scylladb/scylladb-per-partition-rate-limit)
- [ScyllaDB Per Partition Rate Limit Error](/tools/scylladb/scylladb-per-partition-rate-limit-error)
- [ScyllaDB Write Timeout](/tools/scylladb/scylladb-write-timeout)
