---
title: "[Solution] TiDB Placement Policy Error — How to Fix"
description: "Fix TiDB placement policy errors when data placement rules cannot be satisfied across the cluster"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Placement Policy Error

Placement policy errors occur when TiDB cannot satisfy the configured data placement rules, causing regions to be placed in locations that violate constraints.

## Why It Happens

- Placement rules reference labels that do not exist on TiKV nodes
- Insufficient TiKV nodes in the required location
- Label configuration is incorrect or incomplete
- Primary region count exceeds available nodes
- Leader and follower placement rules conflict

## Common Error Messages

```
placement: unable to satisfy rule for table, insufficient nodes with label
```

```
error: placement rule conflict, cannot place region
```

```
PD: label selector matched no stores
```

## How to Fix It

### 1. Check TiKV Labels

```bash
pd-ctl store labels <store_id>
```

### 2. Verify Placement Rules

```sql
SHOW CREATE PLACEMENT POLICY my_policy;
```

### 3. Add Missing Labels

```bash
pd-ctl store add-label <store_id> key=value
```

### 4. Adjust Placement Rules

```sql
CREATE PLACEMENT POLICY my_policy PRIMARY_REGION="zone1" FOLLOWERS=2;
ALTER TABLE mydb.mytable PLACEMENT POLICY=my_policy;
```

## Examples

```
$ pd-ctl store labels 1
{
  "labels": [
    {"key": "zone", "value": "us-east-1a"},
    {"key": "rack", "value": "rack1"}
  ]
}
```

## Prevent It

- Ensure all TiKV nodes have required labels
- Verify placement rules can be satisfied before applying
- Monitor placement rule compliance

## Related Pages

- [TiDB Placement Error](/tools/tidb/tidb-placement-error)
- [TiDB Placement Rule Error](/tools/tidb/tidb-placement-rule-error)
- [TiDB Partition Error](/tools/tidb/tidb-partition-error)
