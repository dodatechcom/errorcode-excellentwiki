---
title: "SQL MERGE Statement Match Conflict Error"
description: "Fix SQL MERGE statement errors when multiple source rows match a single target row causing ambiguous updates."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Multiple source rows match one target row in MERGE
- Duplicate keys in source data
- MERGE with aggregate source that produces multiple matches
- NOT MATCHED clause inserts duplicate rows
- USING clause does not enforce uniqueness

## How to Fix

```sql
-- WRONG: Source has duplicates
MERGE INTO target t
USING source s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET t.value = s.value;
-- ERROR: multiple source rows match same target

-- CORRECT: Deduplicate source first
MERGE INTO target t
USING (SELECT id, MAX(value) AS value FROM source GROUP BY id) s
ON t.id = s.id
WHEN MATCHED THEN UPDATE SET t.value = s.value;
```

```sql
-- WRONG: NOT MATCHED inserts duplicates
MERGE INTO target t
USING source s ON t.id = s.id
WHEN NOT MATCHED THEN INSERT (id, value) VALUES (s.id, s.value);
-- If source has duplicate IDs, inserts multiple rows

-- CORRECT: Add uniqueness check
MERGE INTO target t
USING (SELECT DISTINCT id, value FROM source) s
ON t.id = s.id
WHEN NOT MATCHED THEN INSERT (id, value) VALUES (s.id, s.value);
```

## Examples

```sql
-- Example 1: Basic MERGE upsert
MERGE INTO inventory i
USING (SELECT 'WIDGET' AS sku, 100 AS qty) s
ON i.sku = s.sku
WHEN MATCHED THEN UPDATE SET quantity = quantity + s.qty
WHEN NOT MATCHED THEN INSERT (sku, quantity) VALUES (s.sku, s.qty);

-- Example 2: MERGE with delete
MERGE INTO archive a
USING current_data c ON a.id = c.id
WHEN MATCHED AND c.is_archived = 1 THEN DELETE
WHEN NOT MATCHED AND c.is_archived = 0 THEN INSERT VALUES (c.id, c.data);

-- Example 3: Prevent multiple matches
WITH deduped AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) AS rn
    FROM source
)
MERGE INTO target t
USING deduped s ON t.id = s.id AND s.rn = 1
WHEN MATCHED THEN UPDATE SET t.value = s.value;
```

## Related Errors

- [Merge error](sql-merge-error) -- MERGE statement issues
- [Duplicate entry error](sql-duplicate-entry) -- duplicate data problems
