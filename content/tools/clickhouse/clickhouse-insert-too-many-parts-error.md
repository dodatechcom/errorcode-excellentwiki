---
title: "[Solution] ClickHouse INSERT Too Many Parts Error"
description: "Fix ClickHouse INSERT too many parts errors when inserts create excessive data fragments"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse INSERT Too Many Parts Error

INSERT too many parts errors occur when concurrent inserts create too many unmerged data parts.

## Common Causes

- Too many concurrent INSERT operations
- Each insert creating a single-part batch
- Merge unable to keep up with insert frequency
- Part count exceeding max_parts_per_commit

## How to Fix

Check insert settings:

```sql
SELECT name, value FROM system.settings WHERE name LIKE '%parts_per%';
```

Batch inserts:

```sql
INSERT INTO my_table SELECT * FROM temp_table;
```

Reduce insert frequency:

```python
# Buffer inserts in application
batch = []
for row in data:
    batch.append(row)
    if len(batch) >= 10000:
        client.execute("INSERT INTO my_table VALUES", batch)
        batch = []
```

## Examples

```sql
INSERT INTO my_table SETTINGS max_insert_block_size = 1048576;
```
