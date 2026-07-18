---
title: "[Solution] Cassandra Gossip Error - Fix Gossip Protocol Failure"
description: "Fix Cassandra gossip protocol failures when nodes cannot communicate. Resolve cluster membership, heartbeat, and gossip issues."
tools: ["cassandra"]
error-types: ["gossip-error"]
severities: ["critical"]
weight: 5
---

This error means the Cassandra gossip protocol is failing. Gossip is how nodes share cluster state, detect failures, and maintain membership information.

## What This Error Means

When gossip fails, nodes cannot agree on cluster state:

```
Gossip error: Unable to communicate with seed node
# or
NoNodeAvailableException: No host available for the repair
# or
Gossip status shows nodes as DOWN
```

Gossip runs every second on each node, exchanging heartbeat and state information. When gossip fails, nodes may be incorrectly marked as down.

## Why It Happens

- Network connectivity between nodes is broken
- Firewall rules block the gossip port (7000 or 7000/7001)
- Seed nodes are not configured correctly
- System time is significantly different between nodes
- Too many nodes are down, preventing gossip convergence
- The gossip protocol version is incompatible between nodes

## How to Fix It

### Check cluster status

```bash
nodetool status
```

Look for nodes marked as DN (Down/Normal) or UN (Up/Normal).

### Verify network connectivity

```bash
ping <other-node-ip>
telnet <other-node-ip> 7000
```

### Check firewall rules

```bash
sudo iptables -L -n | grep 7000
sudo firewall-cmd --list-ports
```

Ensure ports 7000 (inter-node) and 7001 (TLS) are open.

### Verify seed node configuration

```yaml
# cassandra.yaml
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
      - seeds: "10.0.0.1,10.0.0.2"
```

All nodes must have the same seed list.

### Restart gossip on a node

```bash
nodetool statusthrift
nodetool resetlocalschema
```

### Check system time synchronization

```bash
# On each node
date
# Verify NTP is running
systemctl status ntpd
```

Gossip uses timestamps to detect stale information.

### Manually mark a node as live

```bash
nodetool info
nodetool status
```

If a node is incorrectly marked down, it may need a restart.

### Increase gossip timeout

```yaml
# cassandra.yaml
gossip_settle_ms: 3000
```

### Use nodetool to check gossip information

```bash
nodetool gossipinfo
```

This shows the state each node has gossiped about.

### Restart a specific node

```bash
sudo systemctl restart cassandra
```

Restarting clears stale gossip state.

## Common Mistakes

- Not having at least two seed nodes for redundancy
- Configuring seeds with private IPs that change in cloud environments
- Not synchronizing system clocks across the cluster
- Ignoring firewall rules between availability zones
- Not monitoring gossip status as part of cluster health checks

## Related Pages

- [Cassandra Connection Error]({{< relref "/tools/cassandra/cassandra-connection-error" >}}) -- connectivity issues
- [Cassandra Unavailable]({{< relref "/tools/cassandra/cassandra-unavailable" >}}) -- availability issues
- [Cassandra Joins Leave]({{< relref "/tools/cassandra/cassandra-joins-leave" >}}) -- node membership
