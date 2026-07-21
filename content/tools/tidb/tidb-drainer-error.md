---
title: "TiDB Drainer Error"
description: "Drainer service failure"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TiDB Drainer (binlog consumer) is failing.

## Common Causes
- Drainer process crashed
- Kafka/MySQL downstream unreachable
- Binlog position too old

## How to Fix
```bash
# Check Drainer status
binlogctl --pd-urls=http://pd:2379 --cmd=status

# Restart Drainer
systemctl restart drainer
```

## Examples
```bash
# Check Drainer logs
tail -100 /var/log/drainer/drainer.log
# Monitor Drainer metrics
curl http://localhost:8249/metrics
```

