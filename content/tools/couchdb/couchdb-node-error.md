---
title: "[Solution] CouchDB Node Error — How to Fix"
description: "Fix CouchDB node errors by recovering from erlang distribution failures, resolving node down status, and rejoining nodes to cluster"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Node Error

CouchDB node errors occur when a node in a clustered CouchDB deployment goes down, becomes unreachable, or fails to join the erlang distribution network.

## Why It Happens

- Erlang distribution cookie is mismatched between nodes
- Network partition prevents node communication
- Node ran out of memory and was killed by OOM killer
- Erlang VM crashed due to large heap allocation
- Port 4369 (epmd) or 9100-9200 (distribution) is blocked
- Hostname resolution fails between nodes

## Common Error Messages

```
{ "error": "nodedown", "reason": "node 'couchdb@node2' is not reachable" }
```

```
{ "error": "internal_server_error", "reason": "cluster_node_down" }
```

```
{ "error": "service_unavailable", "reason": "no_cluster_node_available" }
```

```
{ "error": "not_found", "reason": "missing" }
```

## How to Fix It

### 1. Check Node Status

```bash
# Check if CouchDB is running
sudo systemctl status couchdb

# Check erlang distribution
curl http://localhost:5984/_membership

# Check node status
curl http://localhost:5984/_node/_local
curl http://localhost:5984/_up
```

### 2. Fix Erlang Cookie Mismatch

```bash
# All nodes must share the same erlang cookie
# Check current cookie
cat /opt/couchdb/etc/vm.args | grep -i cookie

# Set the same cookie on all nodes
# In vm.args:
# -setcookie couchdb_secret_cookie

# Restart CouchDB after cookie change
sudo systemctl restart couchdb

# Verify nodes can see each other
curl http://localhost:5984/_membership
```

### 3. Rejoin Node to Cluster

```bash
# On the down node, rejoin the cluster
curl -X PUT http://localhost:5984/_nodes/couchdb@node2 \
  -H "Content-Type: application/json" \
  -d '{"cluster_nodes": {"n": 3, "q": 8, "r": 2, "w": 2}}'

# Force remove a dead node
curl -X DELETE http://localhost:5984/_nodes/couchdb@dead-node

# Add a new node
curl -X PUT http://node1:5984/_nodes/couchdb@node3 \
  -H "Content-Type: application/json" \
  -d '{}'
```

### 4. Fix Network and Port Issues

```bash
# Check erlang port mapper daemon
sudo systemctl status epmd

# Ensure epmd is running on all nodes
epmd -names

# Check distribution ports are open
ss -tlnp | grep -E '(4369|9100|9150)'

# Test connectivity between nodes
ping node2.example.com
nc -zv node2.example.com 5984
```

```bash
# Firewall rules for CouchDB cluster
sudo ufw allow 4369/tcp    # epmd
sudo ufw allow 9100:9200/tcp  # erlang distribution
sudo ufw allow 5984/tcp    # CouchDB HTTP
```

## Common Scenarios

- **Node goes down after config change**: Check erlang cookie and distribution settings.
- **Cluster split-brain**: Ensure quorum is maintained with odd number of nodes.
- **New node won't join**: Verify erlang cookie matches and network connectivity.

## Prevent It

- Use odd number of nodes (3, 5) for proper quorum
- Monitor node health with `_up` and `_membership` endpoints
- Set up automatic node recovery with systemd restart policies

## Related Pages

- [CouchDB Cluster Error](/tools/couchdb/couchdb-cluster-error)
- [CouchDB Shard Error](/tools/couchdb/couchdb-shard-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
