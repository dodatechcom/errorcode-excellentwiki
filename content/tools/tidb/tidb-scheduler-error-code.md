---
title: "TiDB Scheduler Error Code"
description: "Scheduler error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Scheduler returning specific error code.

## Common Causes
- Lock conflict
- Command timeout
- Resource busy

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
# Monitor scheduler duration
curl http://localhost:20180/metrics | grep scheduler_duration
```

