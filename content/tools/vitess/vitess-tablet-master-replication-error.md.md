---
title: "Vitess Tablet Master Replication Error"
description: "Tablet master replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet master replication is failing.

## Common Causes
- Master process crashed
- Master election failed
- Master replication lag

## How to Fix
```bash
# Check master status
vtctlclient ListTablets | grep MASTER

# Check master health
vtctlclient GetShard mykeyspace/0
```

## Examples
```bash
# Check master logs
tail -100 /var/log/vttablet/vttablet.log | grep master
# Monitor master metrics
curl http://localhost:15100/debug/vars | jq '.MasterStatus'
```

