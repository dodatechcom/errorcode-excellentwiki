---
title: "[Solution] Redis Gossip Protocol Communication Error"
description: "How to fix Redis cluster gossip protocol communication failures"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Cluster bus port (port+10000) not reachable between nodes
- Firewall blocking gossip traffic
- Too many nodes causing gossip overhead
- Network latency affecting protocol timing

## Fix

Check gossip port connectivity:

```bash
redis-cli -h node2 -p 17001 PING
```

Verify cluster bus communication:

```bash
sudo tcpdump -i any port 17001
```

Check cluster bus stats:

```bash
redis-cli INFO cluster | grep cluster_slots
```

Ensure all nodes can reach each other:

```bash
for node in node1 node2 node3; do
  redis-cli -h $node -p 17001 PING
done
```

## Examples

```bash
# Check cluster bus stats
redis-cli CLUSTER INFO

# Test bus connectivity
nc -zv node2 17001

# Monitor gossip messages
sudo tcpdump -i any port 17001 -c 20
```
