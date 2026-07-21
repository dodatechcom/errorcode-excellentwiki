---
title: "[Solution] ClickHouse Mutation Error"
description: "Fix ClickHouse mutation errors when ALTER TABLE UPDATE or DELETE operations fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Mutation Error

Mutation errors occur when background mutation operations encounter problems during data modification.

## Common Causes

- Mutation query references non-existent column
- Concurrent mutation on same table
- Mutation timeout exceeded on large datasets
- Insufficient disk space for mutation files

## How to Fix

Check mutation status:

```sql
SELECT * FROM system.mutations WHERE is_done = 0;
```

Kill stuck mutation:

```sql
KILL MUTATION WHERE mutation_id = 'mutation-id';
```

Check mutation progress:

```sql
SELECT database, table, mutation_id, command, create_time, parts_to_do
FROM system.mutations WHERE is_done = 0;
```

## Examples

```sql
ALTER TABLE my_table UPDATE status = 'active' WHERE id < 1000;
```
