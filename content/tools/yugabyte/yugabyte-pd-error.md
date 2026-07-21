---
title: "PD Error"
description: "Placement Driver operation failure"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Placement Driver (PD) is failing operations.

## Common Causes
- PD process crashed
- etcd cluster unhealthy
- Leader election stuck

## How to Fix
```bash
# Check PD status
tiup pd-ctl member

# Restart PD
systemctl restart pd
```

## Examples
```bash
# Check PD logs
tail -100 /var/log/pd/pd.log
# Monitor PD metrics
curl http://localhost:2379/metrics
```

