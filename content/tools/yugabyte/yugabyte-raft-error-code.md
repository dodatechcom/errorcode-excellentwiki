---
title: "YugabyteDB Raft Error Code"
description: "Raft error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Raft consensus returning specific error code.

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
# Monitor raft
curl http://localhost:9000/rpcz | python -m json.tool
# Check tablet leaders
yb-admin list_tablets | grep Leader
```

