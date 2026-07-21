---
title: "[Solution] TiDB Region Scatter Error — How to Fix"
description: "Fix TiDB region scatter errors when PD cannot evenly distribute regions across TiKV nodes"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Region Scatter Error

Region scatter errors occur when PD (Placement Driver) fails to evenly distribute regions across TiKV nodes, causing data hotspot and unbalanced load.

## Why It Happens

- TiKV nodes have different storage capacities
- PD scheduler cannot keep up with region split rate
- Network issues prevent region leader transfer
- Some TiKV nodes are overloaded and reject new regions
- Region scatter operator is disabled in PD

## Common Error Messages

```
region scatter: unable to scatter regions, TiKV nodes unavailable
```

```
PD scheduler: region scatter operator timeout
```

```
error: region distribution is unbalanced
```

## How to Fix It

### 1. Check Region Distribution

```bash
pd-ctl region scatter <region_id>
pd-ctl operator show
```

### 2. Enable Region Scatter

```bash
pd-ctl config set region-scatter-concurrency 16
```

### 3. Manually Scatter Regions

```bash
# Scatter regions on a specific TiKV node
pd-ctl operator add scatter-region <region_id>
```

### 4. Check TiKV Capacity

```bash
pd-ctl store stats <store_id>
```

## Examples

```
$ pd-ctl store stats 1
{
  "store_id": 1,
  "capacity": "100 GiB",
  "available": "50 GiB",
  "region_count": 2000
}
```

## Prevent It

- Ensure TiKV nodes have similar capacity
- Monitor region distribution with PD dashboard
- Enable region scatter scheduler in PD

## Related Pages

- [TiDB Region Error](/tools/tidb/tidb-region-error)
- [TiDB Region Error Code](/tools/tidb/tidb-region-error-code)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
