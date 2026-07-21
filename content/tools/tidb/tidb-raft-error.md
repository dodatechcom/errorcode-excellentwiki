---
title: "TiDB Raft Error"
description: "Raft consensus failure"
tools:
  - tidb
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
curl http://localhost:20180/metrics | grep raft

# Monitor leader
curl http://localhost:20180/metrics | grep raft_leader
```

## Examples
```bash
# Check raft log
curl http://localhost:20180/metrics | grep raft_log
# Monitor election
curl http://localhost:20180/metrics | grep raft_election
```

