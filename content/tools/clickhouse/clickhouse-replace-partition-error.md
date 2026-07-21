---
title: "[Solution] ClickHouse Replace Partition Error"
description: "Fix ClickHouse replace partition errors when REPLACE PARTITION operation fails"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Replace Partition Error

Replace partition errors occur when the ALTER TABLE REPLACE PARTITION command fails.

## Common Causes

- Source partition does not exist
- Target partition has different structure
- Replace operation conflicts with merge
- Partition key type mismatch between tables

## How to Fix

Check partitions in both tables:

```sql
SELECT partition FROM system.parts WHERE table = 'source_table' GROUP BY partition;
SELECT partition FROM system.parts WHERE table = 'target_table' GROUP BY partition;
```

Perform replace:

```sql
ALTER TABLE target_table REPLACE PARTITION '2024-01' FROM source_table;
```

Check for merge conflicts:

```sql
SELECT * FROM system.merges WHERE table = 'target_table';
```

## Examples

```sql
ALTER TABLE target_table REPLACE PARTITION ID '202401' FROM source_table;
```
