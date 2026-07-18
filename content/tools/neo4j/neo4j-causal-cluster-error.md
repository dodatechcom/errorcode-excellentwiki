---
title: "[Solution] Neo4j Causal Cluster Error — How to Fix"
description: "Fix Neo4j Causal Cluster errors including core server failures, read replica issues, and cluster coordination problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Causal Cluster Error

Causal Cluster errors in Neo4j occur when the cluster loses quorum, core servers cannot communicate, or read replicas fall behind. Neo4j Enterprise uses the Raft protocol for consensus.

## Why It Happens

- More than half the core servers are down (loss of quorum)
- Network partition between core servers
- A core server's Raft log is corrupted
- The read replica cannot catch up with the core
- The cluster discovery service is misconfigured
- The `causal_clustering.leader_timeout` is too short

## Common Error Messages

```
Neo.TransientError.Cluster.NotALeader:
No write queries can be served because this server is not the leader
```

```
Neo.TransientError.Cluster.CoreServersUnavailable:
Unable to connect to core servers for the cluster
```

```
Neo.ClientError.Cluster.CoreServerError:
Failed to join cluster: cannot establish discovery
```

```
Neo.TransientError.Cluster.LeaderSwitch:
Leader switch occurred during the transaction
```

## How to Fix It

### 1. Check Cluster Status

```cypher
// Check cluster overview
CALL dbms.cluster.overview();

// Check which servers are core vs read replica
CALL dbms.listConfig() YIELD name, value
WHERE name = 'causal_clustering.minimum_core_cluster_size_at_core'
RETURN value;
```

### 2. Fix Quorum Loss

```bash
# Check which core servers are running
sudo systemctl status neo4j

# Restart core servers one at a time
sudo systemctl start neo4j-core-1
sudo systemctl start neo4j-core-2
sudo systemctl start neo4j-core-3
```

### 3. Fix Leader Election Issues

```bash
# Check cluster logs for election issues
grep -i "leader" /var/log/neo4j/neo4j.log

# Adjust leader timeout in neo4j.conf
causal_clustering.leader_timeout=5s
causal_clustering.catchup_tx_pull_interval=1s
causal_clustering.catchup_batch_size=1024
```

### 4. Fix Read Replica Lag

```bash
# Check read replica lag
grep -i "catchup" /var/log/neo4j/read-replica.log

# Increase catchup resources
causal_clustering.catchup_batch_size=4096
causal_clustering.tx_push_max_batch_size=512
```

## Common Scenarios

- **Core server restarts and cannot rejoin**: The Raft log may be corrupted. Restore from backup or remove and re-add the server.
- **Write queries fail with NotALeader**: Route write queries to the leader server or use the routing driver.
- **Read replica falls behind**: Increase catchup batch size and resources.

## Prevent It

- Run at least 3 core servers for fault tolerance
- Monitor cluster health with `dbms.cluster.overview()`
- Use causal clustering drivers that automatically route to the leader

## Related Pages

- [Neo4j Connection Error](/tools/neo4j/neo4j-connection-error)
- [Neo4j Replication Error](/tools/neo4j/neo4j-replication-error)
- [Neo4j Transaction Error](/tools/neo4j/neo4j-transaction-error)
