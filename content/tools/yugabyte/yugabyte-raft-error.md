---
title: "YugabyteDB Raft Error"
description: "Raft consensus error"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Raft consensus protocol is failing.

## Common Causes
- Leader election timeout
- Quorum lost
- Network partition

## How to Fix
```bash
# Check raft status
curl http://localhost:9000/rpcz

# Force leader election
yb-admin leader_rebalancer
```

## Examples
```bash
# Monitor raft consensus
curl http://localhost:9000/rpcz | python -m json.tool
# Check tablet leaders
yb-admin list_tablets | grep Leader
```

