---
title: "[Solution] ScyllaDB Workload Priority Error — How to Fix"
description: "Fix ScyllaDB workload priority errors when request priority levels are incorrectly assigned or enforced"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Workload Priority Error

Workload priority errors occur when ScyllaDB fails to enforce priority levels between different types of requests, causing latency SLA violations.

## Why It Happens

- Priority levels are not configured in scylla.yaml
- All requests are assigned the same priority
- Priority queue is overwhelmed with high-priority requests
- I/O scheduler cannot differentiate request priorities
- System resources are insufficient for all priority levels

## Common Error Messages

```
Workload priority: unable to schedule request at requested priority
```

```
ERROR: Priority queue overflow, requests degraded to lower priority
```

```
workload_priority: latency SLA exceeded for priority=high requests
```

## How to Fix It

### 1. Configure Priority Levels

```yaml
# In scylla.yaml
scheduling_priority: 1
```

### 2. Set Table-Specific Priorities

```cql
ALTER TABLE mykeyspace.critical_data WITH scheduling_priority = 0;
ALTER TABLE mykeyspace.analytics WITH scheduling_priority = 3;
```

### 3. Monitor Priority Queue Metrics

```bash
curl -s http://localhost:9180/metrics | grep workload_priority
```

### 4. Balance Resource Allocation

```bash
# Ensure sufficient CPU and I/O resources
nproc
cat /proc/cpuinfo | grep processor | wc -l
```

## Examples

```
Workload Priority Distribution:
  Priority 0 (highest): 5000 requests, avg latency 1.2ms
  Priority 1: 15000 requests, avg latency 5.3ms
  Priority 2: 30000 requests, avg latency 25.1ms
  Priority 3 (lowest): 10000 requests, avg latency 150.0ms
```

## Prevent It

- Define clear priority levels for different workload types
- Monitor latency SLAs for each priority level
- Adjust resource allocation based on observed performance

## Related Pages

- [ScyllaDB Workload Prioritization Error](/tools/scylladb/scylladb-workload-prioritization-error)
- [ScyllaDB Workload Prioritization Config Error](/tools/scylladb/scylladb-workload-prioritization-config-error)
- [ScyllaDB CPU Overload](/tools/scylladb/scylladb-cpu-overload)
