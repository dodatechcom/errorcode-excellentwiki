---
title: "[Solution] SQL MERGE Statement Failed Conflict Error Fix"
description: "Fix 'MERGE statement failed' and conflict errors in SQL. Resolve MERGE target source conflicts and duplicate match issues."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL MERGE Statement Failed Conflict Error Fix

The `MERGE statement failed` error occurs when a MERGE (UPSERT) operation encounters conflicting data, duplicate matches, or constraint violations during the merge process.

## What This Error Means

MERGE combines INSERT, UPDATE, and DELETE into a single statement. When multiple source rows match a single target row, or when the merge violates constraints, the operation fails.

A typical error:

```
ERROR: MERGE command failed to update/delete/insert row
DETAIL: A MERGE statement attempted to update the same row more than once
```

## Why It Happens

Common causes include:

- **Duplicate source rows** — Multiple source rows match one target row.
- **Target has duplicates** — Multiple target rows match the source key.
- **Constraint violations** — MERGE inserts data violating UNIQUE or CHECK constraints.
- **Trigger failures** — Triggers on the target table fail during merge.
- **Data type mismatches** — Source and target columns have incompatible types.

## How to Fix It

### Fix 1: Ensure source data is unique

```sql
-- RIGHT: Deduplicate source before merge
MERGE INTO target t
USING (
    SELECT DISTINCT id, name, value
    FROM source
) s ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.name = s.name, t.value = s.value
WHEN NOT MATCHED THEN
    INSERT (id, name, value) VALUES (s.id, s.name, s.value);
```

### Fix 2: Handle multiple matches

```sql
-- RIGHT: Aggregate source to ensure one row per key
MERGE INTO target t
USING (
    SELECT id, MAX(name) AS name, SUM(value) AS value
    FROM source
    GROUP BY id
) s ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.name = s.name, t.value = s.value
WHEN NOT MATCHED THEN
    INSERT (id, name, value) VALUES (s.id, s.name, s.value);
```

### Fix 3: Add WHERE clause to limit matches

```sql
-- RIGHT: Only process valid rows
MERGE INTO target t
USING source s ON t.id = s.id
WHEN MATCHED AND s.status = 'active' THEN
    UPDATE SET t.value = s.value
WHEN NOT MATCHED AND s.status = 'active' THEN
    INSERT (id, value) VALUES (s.id, s.value);
```

### Fix 4: Handle constraint violations

```sql
-- RIGHT: Use NOT MATCHED BY SOURCE for deletions
MERGE INTO target t
USING source s ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.name = s.name
WHEN NOT MATCHED THEN
    INSERT (id, name) VALUES (s.id, s.name)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
```

### Fix 5: Use row versioning for concurrent merges

```sql
-- RIGHT: Add version check
MERGE INTO target t
USING source s ON t.id = s.id
WHEN MATCHED AND t.version < s.version THEN
    UPDATE SET t.name = s.name, t.version = s.version
WHEN NOT MATCHED THEN
    INSERT (id, name, version) VALUES (s.id, s.name, s.version);
```

## Common Mistakes

- **Not deduplicating source data** — MERGE requires one source row per target match.
- **Forgetting WHEN NOT MATCHED** — Missing branch means no inserts.
- **Assuming MERGE is atomic** — Triggers can cause partial failures.

## Related Pages

- [SQL Constraint Error](sql-constraint-error) — Constraint violations
- [SQL Identity Error](sql-identity-error) — Identity column issues
- [SQL Savepoint Error](sql-savepoint-error) — Transaction savepoint issues
