---
title: "SQL DELETE Without LIMIT Performance Error"
description: "Fix SQL DELETE performance errors when deleting large numbers of rows without batching or LIMIT clauses."
languages: ["sql"]
error-types: ["performance-error"]
severities: ["warning"]
weight: 5
---

## Common Causes

- Deleting millions of rows in a single transaction
- DELETE without WHERE clause removes entire table contents
- Large DELETE blocks other transactions due to row locking
- DELETE triggers cascade effects on related tables
- Transaction log fills up during large deletes

## How to Fix

```sql
-- WRONG: Delete millions at once
DELETE FROM logs WHERE created_at < '2023-01-01';
-- May lock table for minutes

-- CORRECT: Batch delete
DELETE FROM logs WHERE created_at < '2023-01-01' LIMIT 10000;
-- Repeat until 0 rows affected
```

```sql
-- WRONG: Deleting all rows with DELETE
DELETE FROM temp_data;
-- Slow for large tables

-- CORRECT: TRUNCATE for full table clear
TRUNCATE TABLE temp_data;
```

## Examples

```sql
-- Example 1: Batched delete procedure
DELIMITER //
CREATE PROCEDURE purge_old_logs()
BEGIN
    DECLARE affected INT DEFAULT 1;
    WHILE affected > 0 DO
        DELETE FROM logs
        WHERE created_at < DATE_SUB(NOW(), INTERVAL 30 DAY)
        LIMIT 5000;
        SET affected = ROW_COUNT();
    END WHILE;
END //
DELIMITER ;

-- Example 2: Delete with JOIN (MySQL)
DELETE l FROM logs l
JOIN archive_status a ON l.id = a.log_id
WHERE a.archived = 1;

-- Example 3: Soft delete instead of hard delete
UPDATE orders SET deleted_at = NOW()
WHERE created_at < '2023-01-01' AND deleted_at IS NULL;
```

## Related Errors

- [Lock timeout error](lock-timeout) -- row locking during delete
- [Transaction error](transaction-error) -- transaction log issues
