---
title: "[Solution] ClickHouse View Not Found Error"
description: "Fix ClickHouse view not found errors when querying non-existent views"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse View Not Found Error

View not found errors occur when queries reference a view that does not exist in the database.

## Common Causes

- View was dropped during migration
- Wrong database name in query
- View name typo
- View created in different database context

## How to Fix

List all views:

```sql
SELECT database, name FROM system.tables WHERE engine IN ('View', 'MaterializedView');
```

Check view definition:

```sql
SELECT name, as_select FROM system.tables WHERE name = 'my_view';
```

Recreate view:

```sql
CREATE VIEW my_view AS SELECT id, name, status FROM source_table WHERE active = 1;
```

## Examples

```sql
SHOW CREATE VIEW my_view;
```
