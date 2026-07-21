---
title: "[Solution] ScyllaDB Read Quorum Error — How to Fix"
description: "Fix ScyllaDB read quorum errors when insufficient replicas respond to satisfy the consistency level"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Read Quorum Error

Read quorum errors occur when ScyllaDB cannot gather enough replica responses to satisfy the requested consistency level for read operations.

## Why It Happens

- Replica nodes are down or unreachable
- Consistency level requires more replicas than are available
- Network latency causes read timeouts before quorum is reached
- Speculative retry threshold is set too low
- Too many concurrent reads overload the coordinator

## Common Error Messages

```
ReadTimeout: Timed out on consistency level LOCAL_QUORUM
```

```
UnavailableException: Cannot achieve consistency level QUORUM
```

```
error: not enough replicas for read at consistency level ALL
```

## How to Fix It

### 1. Lower Consistency Level

```cql
CONSISTENCY ONE;
SELECT * FROM mykeyspace.users WHERE id = 1;
```

### 2. Increase Read Timeouts

```yaml
# In scylla.yaml
read_request_timeout_in_ms: 20000
range_request_timeout_in_ms: 40000
```

### 3. Verify Replica Count

```cql
DESCRIBE KEYSPACE mykeyspace;
```

### 4. Enable Speculative Retry

```cql
ALTER TABLE mykeyspace.users WITH speculative_retry = '95percentile';
```

## Examples

```
ReadTimeout: Error from server: code=1200 [Timeout] ... 
Not enough replicas responded for read at consistency LOCAL_QUORUM (2/3)
```

## Prevent It

- Ensure sufficient replicas for your consistency level
- Monitor replica health across the cluster
- Set appropriate read timeouts for your network

## Related Pages

- [ScyllaDB Read Timeout](/tools/scylladb/scylladb-read-timeout)
- [ScyllaDB Consistency Error](/tools/scylladb/scylladb-consistency-error)
- [ScyllaDB Consistency Level Error](/tools/scylladb/scylladb-consistency-level-error)
