---
title: "TiDB PD Error Code"
description: "PD error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
PD returning specific error code.

## Common Causes
- PD process crashed
- etcd cluster unhealthy
- Leader election stuck

## How to Fix
```bash
# Check PD status
tiup pd-ctl member

# Monitor PD
curl http://localhost:2379/metrics | grep pd
```

## Examples
```bash
# Check PD logs
tail -100 /var/log/pd/pd.log
# Monitor PD metrics
curl http://localhost:2379/metrics | grep -E 'pd|etcd'
```

