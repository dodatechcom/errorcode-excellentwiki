---
title: "YugabyteDB TServer Error Code"
description: "TServer error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TServer returning specific error code.

## Common Causes
- TServer overloaded
- Disk full
- Memory limit

## How to Fix
```bash
# Check TServer status
yb-admin list_tablets

# Monitor TServer
curl http://localhost:9000/metrics | grep tserver
```

## Examples
```bash
# Check TServer logs
tail -100 /home/yugabyte/tserver/logs/yb-tserver.INFO
# Monitor TServer metrics
curl http://localhost:9000/metrics | grep -E 'tserver|tablet'
```

