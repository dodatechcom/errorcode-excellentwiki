---
title: "[Solution] ScyllaDB Per-Partition Rate Limit Error"
description: "How to fix ScyllaDB per-partition rate limiting errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Rate limit too low for workload
- Hot partition hitting rate limit
- Rate limit configuration wrong

## How to Fix

Adjust rate limit:

```yaml
per_partition_rate_limit:
  - {reads: 1000, writes: 1000}
```

## Examples

```bash
grep per_partition_rate /etc/scylla/scylla.yaml
```
