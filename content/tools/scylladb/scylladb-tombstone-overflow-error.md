---
title: "[Solution] ScyllaDB Tombstone Overflow Error — How to Fix"
description: "Fix ScyllaDB tombstone overflow errors when excessive deleted markers cause read performance degradation"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Tombstone Overflow Error

Tombstone overflow errors occur when reads scan too many tombstones (markers for deleted data), causing increased latency and potential query timeouts.

## Why It Happens

- Large number of deletes without proper garbage collection
- TTL expiry creates tombstones faster than they are compacted
- Range deletion removes many rows at once
- Read query scans through data with heavy deletions
- Compaction cannot keep up with tombstone generation

## Common Error Messages

```
ReadTimeout: Scylla timeout during read, data exists but not enough replicas responded
```

```
WARN: Read 100000 live rows and 500000 tombstone cells
```

```
Tombstone overwhelm: query scanned 1000000+ tombstones
```

## How to Fix It

### 1. Limit Query Range

```cql
SELECT * FROM mykeyspace.events 
WHERE user_id = 1 AND event_time > '2024-01-01' AND event_time < '2024-01-02'
LIMIT 1000;
```

### 2. Adjust GC Grace Period

```cql
ALTER TABLE mykeyspace.events WITH gc_grace_seconds = 86400;
```

### 3. Enable Tombstone Warning Threshold

```yaml
# In scylla.yaml
tombstone_warn_threshold: 1000
tombstone_failure_threshold: 100000
```

### 4. Use TWCS for Time-Series Data

```cql
ALTER TABLE mykeyspace.events WITH compaction = {
  'class': 'TimeWindowCompactionStrategy',
  'compaction_window_size': '1',
  'compaction_window_unit': 'DAYS'
};
```

## Examples

```
$ nodetool tablehistograms mykeyspace events
Tombstone cells: 2500000 (warning threshold: 1000)
```

## Prevent It

- Use time-window compaction for TTL-heavy workloads
- Monitor tombstone counts per table
- Design data model to minimize deletes

## Related Pages

- [ScyllaDB Tombstone Overload](/tools/scylladb/scylladb-tombstone-overload)
- [ScyllaDB Tombstone Overload Error](/tools/scylladb/scylladb-tombstone-overload-error)
- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
