---
title: "[Solution] ScyllaDB Gossiper Error"
description: "How to fix ScyllaDB gossip protocol errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Gossip interval too frequent
- Node unable to gossip with peers
- Gossip generation mismatch

## How to Fix

Check gossip status:

```bash
nodetool status
curl http://localhost:10000/gossiper/endpoint/live
```

## Examples

```bash
curl http://localhost:10000/gossiper/endpoint/live
curl http://localhost:10000/gossiper/endpoint/down
```
