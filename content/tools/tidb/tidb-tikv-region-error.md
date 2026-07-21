---
title: "TiDB TiKV Region Error"
description: "TiKV region operation failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TiKV region operation is failing.

## Common Causes
- Region leader unavailable
- Region split/merge conflict
- Scheduler conflict

## How to Fix
```bash
# Check region status
tiup pd-ctl region

# Check region leader
tiup pd-ctl region leader
```

## Examples
```bash
# Check region count
tiup pd-ctl cluster | grep region
# Check region health
tiup pd-ctl operator add scatter-region <region-id>
```

