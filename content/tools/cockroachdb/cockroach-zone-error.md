---
title: "[Solution] CockroachDB Zone Error — How to Fix"
description: "Fix CockroachDB zone configuration errors by correcting zone constraints, resolving replication issues, fixing lease preferences, and managing zone config lifecycle."
tools: ["cockroachdb"]
error-types: ["zone-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB zone error occurs when a zone configuration (replication, constraints, lease preferences) cannot be satisfied by the cluster topology. Zone configurations control how data is distributed across nodes and regions.

## Why It Happens

Zone configurations define the replication factor, data locality, and lease placement for ranges. Errors occur when the cluster topology cannot satisfy these requirements.

- The replication factor exceeds the number of live nodes
- Zone constraints reference datacenter or region names that do not exist
- Lease preferences reference nodes that are decommissioned or down
- The constraint syntax is malformed (e.g., missing brackets, wrong operators)
- Multiple conflicting zone configs are applied to the same table
- The cluster has fewer nodes than the required replication factor
- Nodes in a specified region are overloaded and cannot accept new leases
- Zone configs are applied before the referenced nodes have joined the cluster

## Common Error Messages

```text
ERROR: unable to satisfy zone config for range <range_id>: 
    not enough nodes to satisfy constraints
```

The zone configuration requires more nodes than are available in the specified region or datacenter.

```text
ERROR: zone config constraint "region=us-west1" has no matching nodes
```

No nodes in the cluster have the specified attribute. The constraint name or value is incorrect.

```text
ERROR: lease preferences cannot be satisfied: no nodes match preferences
```

The lease preference references attributes that no available node possesses.

```text
ERROR: replication failed: could not find live replicas for range <range_id>
```

The zone config requires more replicas than there are live nodes.

## How to Fix It

### 1. Check Current Zone Configurations

```sql
-- Show zone config for a database
SHOW ZONE CONFIGURATION FOR DATABASE mydb;

-- Show zone config for a table
SHOW ZONE CONFIGURATION FOR TABLE users;

-- Show all zone configs
SELECT target, config FROM [SHOW ZONE CONFIGURATIONS];
```

```bash
# Check node attributes and locality
cockroach node status --host=localhost:26257 --insecure --format=table

# Check node locality in the node store
ls /var/lib/cockroach/data/
```

### 2. Fix Zone Constraints

```sql
-- Set a zone configuration with correct constraints
ALTER DATABASE mydb CONFIGURE ZONE USING
    num_replicas = 3,
    constraints = '{"+region=us-east1": 1, "+region=eu-west1": 1, "+region=ap-south1": 1}',
    lease_preferences = '[[+region=us-east1]]';

-- Verify the constraints match available nodes
SHOW RANGE FROM TABLE users;

-- List all nodes and their attributes
SELECT node_id, address, locality FROM crdb_internal.gossip_nodes;
```

### 3. Correct Replication Factor

```sql
-- If you have only 2 nodes, RF=3 will fail
-- Reduce RF to match available nodes
ALTER DATABASE mydb CONFIGURE ZONE USING
    num_replicas = 2;

-- If you have 3+ nodes, increase RF for durability
ALTER DATABASE mydb CONFIGURE ZONE USING
    num_replicas = 3;

-- Check if ranges are under-replicated
SELECT range_id, array_length(replicas, 1) as replica_count
FROM crdb_internal.ranges_no_leases
WHERE array_length(replicas, 1) < 3;
```

### 4. Fix Node Locality Attributes

```bash
# Start a node with correct locality
cockroach start \
  --insecure \
  --listen-addr=0.0.0.0:26257 \
  --locality=region=us-east1,rack=rack1 \
  --join=10.0.1.1:26257,10.0.1.2:26257 \
  --store=path=/var/lib/cockroach/data
```

```bash
# Check locality of all nodes
cockroach node status --host=localhost:26257 --insecure --format=csv | \
  awk -F',' '{print $1, $2, $NF}'
```

### 5. Reset Zone Configuration to Default

```sql
-- Reset a database zone config to defaults
ALTER DATABASE mydb CONFIGURE ZONE USING DEFAULT;

-- Reset a table zone config
ALTER TABLE users CONFIGURE ZONE USING DEFAULT;

-- Reset a specific zone
ALTER RANGE default CONFIGURE ZONE USING
    num_replicas = 3,
    gc.ttlseconds = 90000;
```

### 6. Fix Excluded Nodes

```sql
-- If you need to exclude a node from receiving data
ALTER DATABASE mydb CONFIGURE ZONE USING
    num_replicas = 3,
    constraints = '{"+region=us-east1": 2}',
    lease_preferences = '[[+region=us-east1]]';

-- Verify range placement
SHOW RANGES FROM TABLE users;
```

## Common Scenarios

**Zone config applied before nodes exist.** If you set constraints for a region that has no nodes yet, ranges will be under-replicated. Add nodes to the region first, then apply the zone config.

**Changing RF from 3 to 5 requires more nodes.** Increasing the replication factor requires additional nodes. Add nodes to the cluster first, wait for them to join, then update the zone config.

**Conflicting zone configs between database and table.** Table-level configs override database-level configs. If both exist and conflict, the table-level config takes precedence. Review all configs with `SHOW ZONE CONFIGURATIONS`.

## Prevent It

- Always verify node count and locality attributes before applying zone configurations with constraints
- Use `SHOW ZONE CONFIGURATIONS` regularly to audit the current state of all zone configs
- Test zone configuration changes on a staging cluster with the same topology as production
