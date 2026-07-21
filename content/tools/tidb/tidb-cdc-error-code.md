---
title: "TiDB CDC Error Code"
description: "CDC error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
CDC returning specific error code.

## Common Causes
- Kafka producer error
- Consumer lag
- Schema registry error

## How to Fix
```bash
# Check CDC status
tiup cdc list

# Check changefeed errors
tiup cdc query --changefeed-id <id> 2>&1 | grep error
```

## Examples
```bash
# Check Kafka topic
tiup cdc kafka consumer --bootstrap-server localhost:9092 --topic mytopic
# Monitor CDC metrics
curl http://localhost:8301/metrics | grep cdc
```

