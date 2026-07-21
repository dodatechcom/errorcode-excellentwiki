---
title: "TiDB Pump Error"
description: "Pump service failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TiDB Pump (binlog service) is failing.

## Common Causes
- Pump process crashed
- Disk space exhausted
- Drainer connection lost

## How to Fix
```bash
# Check Pump status
binlogctl --pd-urls=http://pd:2379 --cmd=status

# Restart Pump
systemctl restart pump
```

## Examples
```bash
# Check Pump logs
tail -100 /var/log/pump/pump.log
# Monitor Pump metrics
curl http://localhost:8250/metrics
```

