---
title: "Vitess Tablet Replication Replica Error"
description: "Tablet replica replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet replica replication is failing.

## Common Causes
- Replica process crashed
- Replication lag
- Replica not serving traffic

## How to Fix
```bash
# Check replica status
vtctlclient ListTablets | grep REPLICA

# Check replication status
vtctlclient ReplicationStatus <tablet-alias>
```

## Examples
```bash
# Check replica logs
tail -100 /var/log/vttablet/vttablet.log | grep replica
# Monitor replica metrics
curl http://localhost:15100/debug/vars | jq '.ReplicaStatus'
```

