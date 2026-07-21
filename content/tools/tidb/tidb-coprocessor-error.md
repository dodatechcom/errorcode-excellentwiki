---
title: "TiDB Coprocessor Error"
description: "Coprocessor execution failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Coprocessor (TiKV computing) is failing.

## Common Causes
- Coprocessor timeout
- Memory limit exceeded
- Task queue full

## How to Fix
```bash
# Check coprocessor metrics
curl http://localhost:20180/metrics | grep coprocessor

# Monitor task queue
curl http://localhost:20180/metrics | grep coprocessor_pending
```

## Examples
```bash
# Check coprocessor duration
curl http://localhost:20180/metrics | grep coprocessor_duration
# Monitor memory usage
curl http://localhost:20180/metrics | grep coprocessor_memory
```

