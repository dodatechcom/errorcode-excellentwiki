---
title: "[Solution] TiDB PD Scheduler Error — How to Fix"
description: "Fix TiDB PD scheduler errors when the placement driver cannot schedule region operations"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB PD Scheduler Error

PD scheduler errors occur when the Placement Driver cannot properly schedule region operations like splitting, merging, or rebalancing across TiKV nodes.

## Why It Happens

- PD cannot connect to one or more TiKV stores
- Scheduler operators are conflicting with each other
- Region is locked by an ongoing operation
- Store capacity is full and cannot accept new regions
- Scheduler is disabled or misconfigured

## Common Error Messages

```
PD: scheduler unable to create operator for region
```

```
error: region is locked by pending operator
```

```
scheduler: store is unavailable for scheduling
```

## How to Fix It

### 1. Check PD Scheduler Status

```bash
pd-ctl operator show
pd-ctl scheduler show
```

### 2. Remove Stuck Operators

```bash
pd-ctl operator remove <operator_id>
```

### 3. Check Store Status

```bash
pd-ctl store list
pd-ctl store stats <store_id>
```

### 4. Restart PD Scheduler

```bash
# On PD node
pd-ctl scheduler remove grant-leader-scheduler
pd-ctl scheduler add grant-leader-scheduler <store_id>
```

## Examples

```
$ pd-ctl operator show
{
  "operators": [
    {
      "desc": "scatter-region",
      "region_id": 1234,
      "status": "pending"
    }
  ]
}
```

## Prevent It

- Monitor PD scheduler metrics
- Check store health before scheduling operations
- Avoid conflicting operators

## Related Pages

- [TiDB PD Scheduler Error](/tools/tidb/tidb-pd-scheduler-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB Region Error](/tools/tidb/tidb-region-error)
