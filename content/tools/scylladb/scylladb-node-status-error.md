---
title: "[Solution] ScyllaDB Node Status Error — How to Fix"
description: "Fix ScyllaDB node status errors when nodetool status reports unexpected or incorrect node states"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Node Status Error

Node status errors occur when nodetool status reports incorrect or unexpected node states such as DN (Down/Normal), UN (Up/Normal) on a stopped node, or missing nodes.

## Why It Happens

- Gossip has not yet updated node status
- Node crashed without proper decommission
- Network partition isolates a node from the coordinator
- Gossip protocol is slow in large clusters
- Node was forcefully terminated (kill -9)

## Common Error Messages

```
Datacenter: dc1
Status=Up/Down
--  Address    Load       Tokens
DN  10.0.0.3   0 bytes    256
```

```
error: node appears in status DN but is actually running
```

## How to Fix It

### 1. Check Node Process Status

```bash
sudo systemctl status scylla-server
ssh node3 "sudo systemctl status scylla-server"
```

### 2. Force Gossip Update

```bash
# On the node itself
nodetool statusthrift
nodetool statusgossip
```

### 3. Decommission Dead Node

```bash
# If the node is permanently removed
nodetool removenode <host-id>
```

### 4. Reboot and Verify

```bash
sudo systemctl restart scylla-server
sleep 30
nodetool status
```

## Examples

```
$ nodetool status
Datacenter: dc1
===============
Status=Up/Down
--  Address    Load       Tokens  Owns   Host ID
UN  10.0.0.1   1.23 GB    256     33.3%  abc-123
UN  10.0.0.2   1.15 GB    256     33.3%  def-456
DN  10.0.0.3   0 bytes    256     33.3%  ghi-789
```

## Prevent It

- Monitor node health with Scylla Monitoring
- Use Scylla Manager for cluster operations
- Avoid force-killing ScyllaDB processes

## Related Pages

- [ScyllaDB Node Down](/tools/scylladb/scylladb-node-down)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Node Not Joining](/tools/scylladb/scylladb-node-not-joining)
