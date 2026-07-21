---
title: "[Solution] ScyllaDB Read Repair Error — How to Fix"
description: "Fix ScyllaDB read repair errors when the coordinator cannot repair inconsistent replicas during reads"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Read Repair Error

Read repair errors occur when ScyllaDB detects data inconsistency between replicas during a read and fails to automatically repair the differences.

## Why It Happens

- All replicas are down or unreachable for repair
- Read repair timeout is too short for large repairs
- Data inconsistency is too extensive for read repair
- Read repair is disabled but consistency requires it
- Coordinator node is overloaded and cannot coordinate repair

## Common Error Messages

```
Read repair failed: not enough replicas for repair
```

```
WARN: Read repair timed out for table mykeyspace.users
```

```
error: unable to complete read repair, replicas inconsistent
```

## How to Fix It

### 1. Enable Read Repair

```cql
ALTER TABLE mykeyspace.users WITH dclocal_read_repair_chance = 0.1;
```

### 2. Adjust Read Repair Timeout

```yaml
# In scylla.yaml
read_request_timeout_in_ms: 20000
```

### 3. Run Anti-Entropy Repair

```bash
nodetool repair mykeyspace users
```

### 4. Check Replica Health

```bash
nodetool status
nodetool getendpoints mykeyspace users
```

## Examples

```
$ nodetool repair mykeyspace users
[2024-01-15 10:30:00,001] Starting repair #1 for mykeyspace.users
[2024-01-15 10:35:00,001] Repair completed for mykeyspace.users
```

## Prevent It

- Run regular anti-entropy repairs
- Monitor replica consistency across the cluster
- Enable read repair for critical tables

## Related Pages

- [ScyllaDB Read Repair Error](/tools/scylladb/scylladb-read-repair-error)
- [ScyllaDB Read Timeout](/tools/scylladb/scylladb-read-timeout)
- [ScyllaDB Repair Failed](/tools/scylladb/scylladb-repair-failed)
