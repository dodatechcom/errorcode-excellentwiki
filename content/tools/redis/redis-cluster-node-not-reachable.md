---
title: "[Solution] Redis Cluster Node Not Reachable"
description: "How to fix Redis cluster node unreachable errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Node process crashed or was stopped
- Network partition between nodes
- Firewall blocking cluster bus port (port + 10000)
- DNS resolution failure

## Fix

Check if node is running:

```bash
redis-cli -h node-host -p 7001 PING
```

Check cluster bus port:

```bash
ss -tlnp | grep 17001
```

Verify inter-node connectivity:

```bash
redis-cli --cluster check 127.0.0.1:7001
```

Check firewall rules:

```bash
sudo iptables -L -n | grep 7001
```

## Examples

```bash
# Test node connectivity
redis-cli -h 192.168.1.101 -p 7001 PING

# Check cluster bus
redis-cli -h 192.168.1.101 -p 17001 PING

# Verify all nodes see each other
redis-cli CLUSTER NODES | wc -l
```
