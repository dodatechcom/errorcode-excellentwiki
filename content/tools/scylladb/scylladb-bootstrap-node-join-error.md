---
title: "[Solution] ScyllaDB Bootstrap Node Join Error — How to Fix"
description: "Fix ScyllaDB bootstrap node join errors when new nodes fail to complete the cluster join process"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Bootstrap Node Join Error

Bootstrap node join errors occur when a new ScyllaDB node cannot complete the join process after being started with the --join-cluster flag.

## Why It Happens

- Existing cluster nodes cannot be reached
- Token ranges are not assigned correctly
- Schema version does not match the cluster
- Gossip cannot establish communication
- The node was previously in the cluster with the same token

## Common Error Messages

```
error: unable to join cluster, no seeds reachable
```

```
Bootstrap: token assignment failed
```

```
error: node already exists in cluster with same token
```

## How to Fix It

### 1. Check Seed Node Accessibility

```bash
# From the new node
nc -zv seed-node1 7000
nc -zv seed-node2 7000
```

### 2. Verify Token Assignment

```bash
# Check if the token is already in use
nodetool ring
```

### 3. Remove Old Node Entry

```bash
# If the node was previously in the cluster
nodetool removenode <old-host-id>
```

### 4. Start Fresh Bootstrap

```bash
# Remove old data and try again
sudo rm -rf /var/lib/scylla/data/*
scylla --join-cluster
```

## Examples

```
$ nodetool ring
Address     DC          Rack        Token
10.0.0.1    us-east-1   rack1       -9223372036854775808
10.0.0.2    us-east-1   rack1       -4611686018427387904
10.0.0.3    us-east-1   rack1       0
-- new node 10.0.0.4 should get 4611686018427387904
```

## Prevent It

- Ensure seed nodes are listed in the new node's configuration
- Check that the node's IP is not already in the cluster
- Use Scylla Manager for node lifecycle management

## Related Pages

- [ScyllaDB Bootstrap Error](/tools/scylladb/scylladb-bootstrap-error)
- [ScyllaDB Bootstrap Failed](/tools/scylladb/scylladb-bootstrap-failed)
- [ScyllaDB Node Not Joining](/tools/scylladb/scylladb-node-not-joining)
