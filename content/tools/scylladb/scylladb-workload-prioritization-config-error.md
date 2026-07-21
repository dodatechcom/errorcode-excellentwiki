---
title: "[Solution] ScyllaDB Workload Prioritization Error — How to Fix"
description: "Fix ScyllaDB workload prioritization errors when request scheduling fails to meet latency targets"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Workload Prioritization Error

Workload prioritization errors occur when ScyllaDB fails to properly schedule requests across different workload classes, causing latency targets to be missed.

## Why It Happens

- Workload classes are not configured in scylla.yaml
- Request scheduling weights are unbalanced
- Too many high-priority requests starve low-priority ones
- I/O scheduler cannot differentiate between workload classes
- System resources are insufficient for all workload classes

## Common Error Messages

```
workload_priority: unable to schedule request, priority queue full
```

```
ERROR: Workload class "oltp" exceeded latency SLA by 200%
```

```
Request scheduling failed: no available workload class for request
```

## How to Fix It

### 1. Configure Workload Classes

```yaml
# In scylla.yaml
workload_classes:
  - name: oltp
    shares: 100
  - name: olap
    shares: 50
  - name: analytics
    shares: 25
```

### 2. Assign Tables to Workload Classes

```cql
ALTER TABLE mykeyspace.users WITH workload_class = 'oltp';
ALTER TABLE mykeyspace.reports WITH workload_class = 'analytics';
```

### 3. Monitor Workload Latency

```bash
nodetool workloadstats
curl -s http://localhost:9180/metrics | grep workload_latency
```

### 4. Adjust Priority Weights

```yaml
# In scylla.yaml
workload_oltp_shares: 100
workload_olap_shares: 50
workload_streaming_shares: 25
```

## Examples

```
Workload: oltp, Requests: 150000, Avg Latency: 2.3ms (target: 5ms) OK
Workload: analytics, Requests: 5000, Avg Latency: 450ms (target: 200ms) EXCEEDED
```

## Prevent It

- Define clear latency SLAs for each workload class
- Monitor workload class performance continuously
- Adjust shares based on observed behavior

## Related Pages

- [ScyllaDB Workload Prioritization Error](/tools/scylladb/scylladb-workload-prioritization-error)
- [ScyllaDB Query Timeout Error](/tools/scylladb/scylladb-query-timeout-error)
- [ScyllaDB CPU Overload](/tools/scylladb/scylladb-cpu-overload)
