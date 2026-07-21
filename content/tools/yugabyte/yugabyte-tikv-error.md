---
title: "TiKV Error"
description: "TiKV storage engine error"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TiKV node is experiencing errors.

## Common Causes
- TiKV process crashed
- Disk space exhausted
- Memory pressure

## How to Fix
```bash
# Check TiKV status
tiup pd-ctl store

# Restart TiKV
systemctl restart tikv
```

## Examples
```bash
# Check TiKV logs
tail -100 /var/log/tikv/tikv.log
# Monitor TiKV metrics
curl http://localhost:20180/metrics
```

