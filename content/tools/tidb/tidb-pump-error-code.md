---
title: "TiDB Pump Error Code"
description: "Pump error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Pump returning specific error code.

## Common Causes
- Pump process crashed
- Disk space exhausted
- Drainer connection lost

## How to Fix
```bash
# Check Pump status
binlogctl --pd-urls=http://pd:2379 --cmd=status

# Monitor Pump
curl http://localhost:8250/metrics | grep pump
```

## Examples
```bash
# Check Pump logs
tail -100 /var/log/pump/pump.log
# Monitor Pump metrics
curl http://localhost:8250/metrics | grep -E 'pump|binlog'
```

