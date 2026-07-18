---
title: "[Solution] TiDB Placement Error — How to Fix"
description: "Fix TiDB placement errors by resolving placement rule failures, fixing label constraints, and handling region placement issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Placement Error

TiDB placement errors occur when data placement rules cannot be satisfied. Placement rules control where data replicas are stored across zones and regions.

## Why It Happens

- Placement rules require more replicas than available nodes
- Label constraints cannot be satisfied by any store
- Region leader is not in the preferred zone
- Placement rules conflict with replication factor
- Store labels are not configured correctly
- Placement rule priority is misconfigured

## Common Error Messages

```
ERROR: placement rules not satisfied
```

```
ERROR: no store available for placement
```

```
ERROR: region placement violation
```

```
WARNING: leader not in preferred zone
```

## How to Fix It

### 1. Check Placement Rules

```bash
# Check placement rules
curl http://pd1:2379/pd/api/v1/config/rules

# Check store labels
curl http://pd1:2379/pd/api/v1/stores | jq '.stores[].labels'
```

### 2. Configure Placement Rules

```bash
# Enable placement rules
curl -X POST http://pd1:2379/pd/api/v1/config/rules/enable -d '{"enable": true}'

# Set placement rule for database
curl -X POST http://pd1:2379/pd/api/v1/config/rules -d '{
  "group_id": "zone",
  "id": "zone1",
  "index": 0,
  "override": true,
  "label_constraints": [{"key": "zone", "values": ["zone1"]}],
  "count": 2
}'
```

### 3. Fix Store Labels

```bash
# Set store labels
curl -X POST http://pd1:2379/pd/api/v1/store/1/labels -d '{
  "labels": [
    {"key": "zone", "value": "zone1"},
    {"key": "region", "value": "us-east"}
  ]
}'
```

### 4. Monitor Placement

```bash
# Check region placement
curl http://pd1:2379/pd/api/v1/regions | jq '.regions[0].peers'

# Check placement rule status
curl http://pd1:2379/pd/api/v1/config/rules
```

## Common Scenarios

- **Placement rules not satisfied**: Add more nodes in required zones.
- **Leader not in preferred zone**: Check PD scheduling and store labels.
- **Placement conflicts with RF**: Adjust placement rules to match replication factor.

## Prevent It

- Configure store labels before setting placement rules
- Ensure enough nodes in each zone for placement requirements
- Monitor placement rule compliance

## Related Pages

- [TiDB Region Error](/tools/tidb/tidb-region-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB Partition Error](/tools/tidb/tidb-partition-error)
