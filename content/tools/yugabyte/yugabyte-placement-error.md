---
title: "[Solution] YugabyteDB Placement Error — How to Fix"
description: "Fix YugabyteDB placement errors by resolving tablet placement constraints, fixing cloud region configuration, and handling geo-partitioning issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Placement Error

YugabyteDB placement errors occur when tablet replicas are not placed according to the configured placement constraints. Placement ensures data is distributed across fault domains.

## Why It Happens

- Not enough nodes in a zone/region for replication factor
- Placement policy conflicts with available nodes
- Cloud provider AZ does not have enough capacity
- Tablet leaders are not evenly distributed
- Geo-partitioning constraints cannot be satisfied
- Placement info is misconfigured in Master

## Common Error Messages

```
ERROR: not enough nodes in zone for replication
```

```
ERROR: placement constraint cannot be satisfied
```

```
ERROR: tablet placement violation
```

```
WARNING: uneven tablet leader distribution
```

## How to Fix It

### 1. Check Placement Configuration

```bash
# Check placement info
/home/yugabyte/master/bin/yb-admin get_cluster_config | grep placement

# List nodes by zone
curl http://yb-master-1:7000/cluster-config | jq '.tablet_servers[] | {uuid, placement_uuid, zone}'
```

### 2. Configure Placement

```bash
# In master.gflags:
--placement_zone=us-east-1a
--placement_region=us-east-1
--placement_cloud=aws

# Set cloud info for each node
# Ensure all nodes in same AZ have same placement info
```

### 3. Fix Tablet Leader Distribution

```bash
# Check leader distribution
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers

# Move tablet leaders to balance
/home/yugabyte/tserver/bin/yb-admin move_tablet_leader <tablet_id> <dest_tserver>
```

### 4. Configure Geo-Partitioning

```sql
-- Create table with tablespace for placement
CREATE TABLE customer_data (
  customer_id UUID NOT NULL,
  data JSONB,
  PRIMARY KEY (customer_id)
) TABLESPACE us_east_tablespace;

-- Create tablespace with placement
CREATE TABLESPACE us_east_tablespace WITH (
  replica_placement = '{"num_replicas": 3, "placement_blocks": [{"cloud": "aws", "region": "us-east-1", "zone": "us-east-1a", "min_replicas": 1}, {"cloud": "aws", "region": "us-east-1", "zone": "us-east-1b", "min_replicas": 1}, {"cloud": "aws", "region": "us-east-1", "zone": "us-east-1c", "min_replicas": 1}]}'
);
```

## Common Scenarios

- **Replicas not balanced across zones**: Add nodes to under-represented zones.
- **Geo-partitioning fails**: Ensure enough nodes in each target zone.
- **Leader skew**: Use tablet leader movement to balance.

## Prevent It

- Ensure adequate nodes in each zone for replication factor
- Monitor placement with cluster config endpoint
- Use tablespace for geo-partitioned tables

## Related Pages

- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Replication Error](/tools/yugabyte/yugabyte-replication-error)
- [YugabyteDB Cluster Error](/tools/yugabyte/yugabyte-federation-error)
