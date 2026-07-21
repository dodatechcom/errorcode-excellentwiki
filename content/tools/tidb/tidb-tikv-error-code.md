---
title: "TiKV Error Code"
description: "TiKV error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TiKV returning specific error code.

## Common Causes
- TiKV process crashed
- Disk space exhausted
- Memory pressure

## How to Fix
```bash
# Check TiKV status
tiup pd-ctl store

# Monitor TiKV
curl http://localhost:20180/metrics | grep tikv
```

## Examples
```bash
# Check TiKV logs
tail -100 /var/log/tikv/tikv.log
# Monitor TiKV metrics
curl http://localhost:20180/metrics | grep -E 'tikv|raft'
```

