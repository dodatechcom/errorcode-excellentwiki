---
title: "[Solution] ScyllaDB Read Timeout Error"
description: "How to fix ScyllaDB read timeout errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Replica node slow to respond
- Query scanning too much data
- read_request_timeout_in_ms too low
- Network latency between coordinator and replica

## How to Fix

Increase timeout:

```yaml
read_request_timeout_in_ms: 10000
```

Optimize query:

```cql
-- Add LIMIT
SELECT * FROM my_table WHERE id = 1 LIMIT 100;
```

## Examples

```bash
grep read_request_timeout /etc/scylla/scylla.yaml
```
