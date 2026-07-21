---
title: "TiDB Scheduler Error"
description: "Scheduler operation failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TiKV scheduler is failing operations.

## Common Causes
- Scheduler busy
- Lock conflict
- Command queue full

## How to Fix
```bash
# Check scheduler metrics
curl http://localhost:20180/metrics | grep scheduler

# Monitor command queue
curl http://localhost:20180/metrics | grep command
```

## Examples
```bash
# Check scheduler pending
curl http://localhost:20180/metrics | grep scheduler_pending
# Monitor command duration
curl http://localhost:20180/metrics | grep command_duration
```

