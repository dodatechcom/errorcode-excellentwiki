---
title: "TiDB PD Scheduler Error"
description: "PD scheduler operation failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
PD scheduler operation is failing.

## Common Causes
- Scheduler busy
- Region not found
- Store unavailable

## How to Fix
```bash
# Check scheduler status
tiup pd-ctl scheduler show

# Check store status
tiup pd-ctl store
```

## Examples
```bash
# Check scheduler pending
curl http://localhost:2379/metrics | grep scheduler
# Monitor scheduler
curl http://localhost:2379/metrics | grep region
```

