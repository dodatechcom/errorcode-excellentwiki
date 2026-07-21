---
title: "TiDB Drainer Error Code"
description: "Drainer error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Drainer returning specific error code.

## Common Causes
- Drainer process crashed
- Kafka/MySQL downstream unreachable
- Binlog position too old

## How to Fix
```bash
# Check Drainer status
binlogctl --pd-urls=http://pd:2379 --cmd=status

# Monitor Drainer
curl http://localhost:8249/metrics | grep drainer
```

## Examples
```bash
# Check Drainer logs
tail -100 /var/log/drainer/drainer.log
# Monitor Drainer metrics
curl http://localhost:8249/metrics | grep -E 'drainer|binlog'
```

