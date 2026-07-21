---
title: "YugabyteDB Master Error Code"
description: "Master error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Master returning specific error code.

## Common Causes
- Master overloaded
- Metadata corruption
- Leader election

## How to Fix
```bash
# Check master status
yb-admin list_masters

# Monitor master
curl http://localhost:7000/metrics | grep master
```

## Examples
```bash
# Check master logs
tail -100 /home/yugabyte/master/logs/yb-master.INFO
# Monitor master metrics
curl http://localhost:7000/metrics | grep -E 'master|leader'
```

