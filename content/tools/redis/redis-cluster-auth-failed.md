---
title: "[Solution] Redis Cluster AUTH Failed Error"
description: "How to fix Redis cluster authentication failures between nodes"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Cluster nodes have different passwords
- CLUSTER-AUTH password not configured
- ACL credentials mismatch between nodes

## Fix

Set cluster auth password on all nodes:

```bash
redis-cli -h node1 -p 7001 CONFIG SET cluster-require-full-coverage yes
```

Ensure all nodes have same password:

```bash
# Set on all nodes
redis-cli -h node1 -p 7001 CONFIG SET requirepass "samepassword"
redis-cli -h node2 -p 7002 CONFIG SET requirepass "samepassword"
redis-cli -h node3 -p 7003 CONFIG SET requirepass "samepassword"
```

Update redis.conf on all nodes:

```bash
cluster-auth-pass samepassword
```

## Examples

```bash
# Test node auth
redis-cli -h node1 -p 7001 -a samepassword PING

# Check cluster auth config
redis-cli CONFIG GET cluster-auth

# Test inter-node communication
redis-cli --cluster check 127.0.0.1:7001 -a samepassword
```
