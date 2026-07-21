---
title: "Vitess Tablet Replication Spare Error"
description: "Tablet spare replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet spare replication is failing.

## Common Causes
- Spare tablet not found
- Spare tablet health issue
- Spare tablet configuration error

## How to Fix
```bash
# Check spare tablets
vtctlclient ListTablets | grep SPARE

# Check tablet health
vtctlclient ListTablets
```

## Examples
```bash
# Check spare tablet logs
tail -100 /var/log/vttablet/vttablet.log | grep spare
# Monitor spare tablet metrics
curl http://localhost:15100/debug/vars | jq '.SpareTablets'
```

