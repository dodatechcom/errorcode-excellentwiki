---
title: "YugabyteDB Replication Error Code"
description: "Replication error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Replication failing with specific error code.

## Common Causes
- Raft follower unreachable
- Replication queue full
- Clock skew

## How to Fix
```bash
# Check replication status
curl http://localhost:9000/rpcz

# Force tablet move
yb-admin move_tablet
```

## Examples
```bash
# Check replication lag
curl http://localhost:9000/metrics | grep replication_lag
# Monitor follower state
curl http://localhost:9000/rpcz | python -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2))"
```

