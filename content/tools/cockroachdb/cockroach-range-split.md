---
title: "[Solution] CockroachDB Range Split Error - Fix Range Split Failed"
description: "Fix CockroachDB range split failures. Resolve range boundaries, manual splits, and range size issues in CockroachDB."
tools: ["cockroachdb"]
error-types: ["range-split"]
severities: ["error"]
weight: 5
---

This error means a CockroachDB range split operation failed. Ranges are the fundamental unit of data distribution, and split failures can cause hotspots.

## What This Error Means

When a range split fails, you see:

```
ERROR: range already split
# or
ERROR: split failed: key is not in the range
# or
ERROR: could not find valid split key
```

CockroachDB automatically splits ranges when they grow large, but manual splits or automatic splits can fail for various reasons.

## Why It Happens

- The range is already at the minimum size and cannot be split
- The proposed split key is outside the range boundaries
- The range is too small to split further
- A schema change is in progress on the table
- The split would create ranges that are too small
- The node hosting the range is overloaded

## How to Fix It

### Check range status

```sql
SELECT range_id, start_key, end_key, lease_holder, replicas
FROM [SHOW RANGES FROM TABLE orders];
```

### Manually split a range

```sql
ALTER TABLE orders SPLIT AT SELECT id FROM orders WHERE id = 100000;
```

This splits the table at the specified key.

### Check range size

```sql
SELECT range_id,
  ROUND(range_size_mb, 2) AS size_mb
FROM [SHOW RANGES FROM TABLE orders]
ORDER BY range_size_mb DESC;
```

Ranges larger than 512MB are automatically split.

### Monitor range distribution

```sql
SELECT * FROM crdb_internal.ranges
WHERE table_name = 'orders'
ORDER BY start_key;
```

### Merge small ranges

```sql
ALTER TABLE orders MERGE (SELECT * FROM [SHOW RANGES FROM TABLE orders]
  WHERE range_size_mb < 10);
```

### Fix hotspots with manual splits

```sql
-- Split at frequent access points
ALTER TABLE orders SPLIT AT VALUES ('2024-01-01'), ('2024-07-01');
```

### Check for range lease issues

```sql
SELECT range_id, lease_holder, lease_expiration
FROM [SHOW RANGES FROM TABLE orders]
WHERE lease_holder IS NULL;
```

### Rebalance ranges across nodes

```sql
-- CockroachDB automatically rebalances
-- Check with
SHOW NODE TREETABLES;
```

### Monitor automatic splits

```sql
SHOW CLUSTER SETTING range.split.by_load_enabled;
```

### Use partitioning for large tables

```sql
ALTER TABLE orders PARTITION BY LIST (region) (
  PARTITION us VALUES IN ('us-east', 'us-west'),
  PARTITION eu VALUES IN ('eu-west', 'eu-central')
);
```

## Common Mistakes

- Not monitoring range sizes for large tables
- Assuming automatic splits will always work correctly
- Not partitioning large tables by region or time
- Forgetting that range splits can temporarily affect performance
- Not checking range lease distribution after splits

## Related Pages

- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
- [CockroachDB Node Unavailable]({{< relref "/tools/cockroachdb/cockroach-node-unavailable" >}}) -- node issues
- [CockroachDB Range Split]({{< relref "/tools/cockroachdb/cockroach-range-split" >}}) -- range issues
